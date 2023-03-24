from django.shortcuts import redirect
from rest_framework import viewsets, mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from main import serializers
import django_filters.rest_framework
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from main.integrations.payku import payku
from main.integrations.omnisend import Omnisend
from main.integrations.chipax import Chipax
from main.integrations.lioren import Lioren
from main.integrations.tradegecko import tradegecko
from django.views.decorators.csrf import csrf_exempt
from celery import current_app
from .tasks import odoo_sync
import json, random, string
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login
from sentry_sdk import capture_exception
from django.conf import settings
from time import sleep

class storeView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = storeSerializer

class tiendasView(viewsets.ModelViewSet):
    pagination_class = None
    queryset = puntosVentas.objects.all()
    serializer_class = puntosVentasSerializer
    filterset_fields = ['nombre', 'direccion']
class productView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    filterset_fields = ['is_masvendido', 'is_destacado', "id", "category","store"]

class imageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = imageSerializer

class contactformView(viewsets.ModelViewSet):
    queryset = Contactform.objects.all()
    serializer_class = contactformSerializer

class sliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = sliderSerializer

class blogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    filterset_fields = ['id','created_at','tags','category',"store"]

class recipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = recipeSerializer
    filterset_fields = ['tags', 'created_at','category',"store"]

class RecetasApiView(generics.RetrieveAPIView):

    queryset = Recipe.objects.all()

    def get(self, *arg, **kwargs):
        print(kwargs.get('url'))
        articulo = Recipe.objects.get(slug=kwargs.get('url'))
        all_art = self.queryset.order_by('-id')[:5]
        response = {}
        response['receta'] = recipeSerializer(articulo).data
        response['relacionados'] = recipeSerializer(all_art, many=True).data
        return Response(response)

class categoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categorySerializer

class tagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = tagSerializer

class ProcategoryView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = categorySerializer

class lineitemView(viewsets.ModelViewSet):
    queryset = Lineitem.objects.all()
    serializer_class = lineitemSerializer

class shippingView(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = shippingSerializer

class addressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = addressSerializer
    filterset_fields = ['user']


class orderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = orderSerializer
    filterset_fields = ['id','created_at','user', 'order_number']


    def create(self, request, *arg,**kwargs):
        mailclient = Omnisend()
        data_info_str = request.data
        if isinstance(data_info_str, str):
            data_info = json.loads(data_info_str)
        else:
            data_info = data_info_str
        id_usuario = data_info['user_id']
        usuario = User.objects.get(id=id_usuario)
        print(usuario)
        metodopago =data_info['payment_method']
        internal_status = 'Pendiente pago'
        status = 'Pendiente Pago'
        print(request.data)
        store = get_object_or_404(Store, id=data_info['cart'][0]['product']['store'])
        try:
            ultimo_record = Order.objects.latest('id')
            numero_orden = ultimo_record.order_number + 1
        except ObjectDoesNotExist as e:
            capture_exception(e)
            numero_orden = 4000 + 1
        address = Address.objects.create(user_id=id_usuario, 
                                         name='despacho',
                                         country='Chile', 
                                         state=data_info['address']['state'],
                                         city=data_info['address']['city'], 
                                         comuna=data_info['address']['comuna'],
                                         street=data_info['address']['street'], 
                                         number=data_info['address']['number'],
                                         zipcode=data_info['address']['zipcode'],
                                         rut = data_info['address']['rut'],
                                         mobile=data_info['address']['mobile'])
        new_cart = Order.objects.create()
        items_para_omnisend = []
        for index, productoctm in enumerate(data_info['cart']):
            prod = Product.objects.get(id=productoctm['product']['id'])
            items_para_omnisend.append({'productID':prod.mailchimp_id,
                                        'variantID': Omnisend().getProduct(prod.mailchimp_id)['variants'][0]['variantID'],
                                        'title': prod.name,
                                        'quantity':productoctm['quantity'],
                                        'price':prod.price})
            lineitems,created = Lineitem.objects.get_or_create(
                        product=prod,
                        quantity=productoctm['quantity']
                    )
            new_cart.products.add(lineitems.id)
        new_cart.address = address
        new_cart.store = store
        new_cart.user = usuario
        new_cart.order_number = numero_orden
        new_cart.payment_method = metodopago
        new_cart.sales_tax = store.sales_tax
        new_cart.internal_status = internal_status
        new_cart.shipping_cost = data_info['Shipping']
        shipingOkject = Shipping.objects.filter(price=data_info['Shipping'])
        new_cart.shipping_id = shipingOkject[0].id
        new_cart.status = status
        if store.location == 'CL':
            new_cart.total_gross = int(round(data_info['Total']/(1+store.sales_tax),0))
            new_cart.total_net = data_info['Total']
        else:
            new_cart.total_gross = int(round(data_info['Total']/(1+store.sales_tax),0))
            new_cart.total_net = data_info['Total']
            #new_cart.total_gross = data_info['Total']
            #new_cart.total_net = data_info['Total']*(1+store.sales_tax)
        new_cart.save()

        #creating order in omnisend
        tax = float(data_info['Total'])*1.19
        if metodopago == 99:
            respuestaomnisend = Omnisend().AddOrder(items_para_omnisend, usuario.mailchimp_id, numero_orden, data_info['SubTotal'],data_info['Total'],0,tax,data_info['Shipping'],'awaitingPayment')
            new_cart.mailchimp_id = respuestaomnisend
        new_cart.save()

        #redirect to payku
        paykuApi = payku()
        try:
            payku_response = paykuApi.Pagocontarjeta(usuario.email,data_info['Total'],numero_orden,"Tienda Kokorofoods",metodopago )
        except Exception as e:
            capture_exception(e)
        return Response(payku_response)


@csrf_exempt
def retornopayku(request):
    respuesta = json.loads(request.body)    
    print(respuesta)
    #return HttpResponse()
    orden_actual = get_object_or_404(Order, order_number=respuesta['order'])
    if orden_actual.lioren_id:
        return HttpResponse()
    else:
        orden_actual.payku_transaction_id = respuesta['transaction_id']
        orden_actual.payku_verification_key = respuesta['verification_key']
        if respuesta['status'] != 'success':
            orden_actual.status = 'Pago rechazado'
            orden_actual.internal_status = 'Pago Rechazado'
        else:                
            orden_actual.status = 'Pago Confirmado'
            orden_actual.internal_status = 'Pago Confirmado'
            store = get_object_or_404(Store, id=orden_actual.store.id)
            lineItem = Lineitem.objects.filter(order__id=orden_actual.id)
            items_para_omnisend = []
            for item in lineItem: 
                items_para_omnisend.append({'productID':item.product.mailchimp_id,
                                            'variantID': Omnisend().getProduct(item.product.mailchimp_id)['variants'][0]['variantID'],
                                            'title': item.product.name,
                                            'quantity':item.quantity,
                                            'price':item.product.price})
            try:
                respuestaomnisend = Omnisend().AddOrder(items_para_omnisend, orden_actual.user.mailchimp_id, orden_actual.order_number, orden_actual.total_gross, orden_actual.total_net,0, orden_actual.sales_tax, orden_actual.shipping_cost,'paid')
                orden_actual.mailchimp_id = respuestaomnisend
            except KeyError as e:
                capture_exception(e)
            # agregando chipax
            if orden_actual.discount == 'null':
                discount = 0
            else:
                discount = orden_actual.discount
            items_chipax = []
            items_lioren = []
            # items_tradegecko = []
            for cadaitem in orden_actual.products.all():
                unitario, estado = Lineitem.objects.get_or_create(id=cadaitem.id)
                item = Product.objects.get(id=unitario.product.id)
                line = {"cantidad": unitario.quantity,
                        "fecha": orden_actual.created_at.strftime("%Y-%m-%d"),
                        "descuento": discount,
                        "descripcion" : item.name,
                        "linea_negocio_id": 10508,
                        "moneda_id": 1000,
                        "precio_unitario": item.price,
                        "producto_id": 13068,
                        "valor_moneda": 1
                    }
                temp = {'codigo': item.name,
                        'nombre': item.name,
                        'cantidad': unitario.quantity,
                        'precio':item.price,
                        'exento':False}
                # temp2 = {"variant_id":tradegecko().getProduct(item.tradegecko_id)['product']["variant_ids"][0],
                #         "quantity":unitario.quantity,
                #         "tax_type_id": 389061,
                #         "price":item.price}
                items_lioren.append(temp)
                items_chipax.append(line)
                # items_tradegecko.append(temp2)
                item.quantity = item.quantity - unitario.quantity
                item.save()
            # shippingItem = {
            #     "freeform": True,
            #     "line_type": "shipping",
            #     "tax_type_id": 389061,
            #     "label": orden_actual.shipping.description,
            #     "price": orden_actual.shipping_cost,
            #     "quantity": "1.0",
            #     "tax_rate_override": "0.0",
            #     "tax_rate": "0.0"
            # }
            # items_tradegecko.append(shippingItem)
            chip = Chipax()
            token = chip.login()
            chipax_info = {"cliente_id": 1712910,
                            "fecha": orden_actual.created_at.strftime("%Y-%m-%d"),
                            "fecha_pago": datetime.now().strftime("%Y-%m-%d"),
                            "iva": 19,
                            "nota": "Venta n° " +str(respuesta['order']),
                            "moneda_id": 1000,
                            "monto_total": orden_actual.total_gross,
                            "monto_neto": str(orden_actual.total_net),
                            "exenta": False,
                            "otro_ingreso": False,
                            "documentos_referencia": [],
                            "items": items_chipax,
                            "Saldo": {"saldo_deudor": orden_actual.total_gross,
                                    "saldo_acreedor": 0
                                }  
                        }
            respuestachipax = chip.createNotasVenta(token, chipax_info)
            liorenapp = Lioren()
            customer = User.objects.get(id=orden_actual.user.id)
            receptor = {
                        'rs': customer.first_name + ' ' + customer.last_name,
                        'email': customer.email
                        }
            if orden_actual.shipping_cost > 0:
                temp = {'codigo': "Costo de envio",
                        'nombre': "Costo de envio",
                        'cantidad': 1,
                        'precio':orden_actual.shipping_cost,
                        'exento':False}
                items_lioren.append(temp)
            try:
                respuestalioren = liorenapp.registrarBoleta(items_lioren, receptor)
                orden_actual.lioren_id = respuestalioren['id']
                orden_actual.folio_sii = respuestalioren['folio']
                orden_actual.boleta_pdf = respuestalioren['pdf']
            except KeyError as e:
                capture_exception(e)
            # print('crenado orden en tradegecko')
            # creando orden en Tradegecko
            # direccion = orden_actual.address
            # print(direccion.tradegecko_id)
            # if direccion.tradegecko_id is None:
            #     usuario = orden_actual.user
            #     print('direccion sin tradegecko id',usuario)
            #     if usuario.tradegecko_id is None:
            #         print('usuario sin tradegecko id')
            #         respuesta = tradegecko().getCustomerbyEmail(usuario.email)
            #         if not respuesta['companies']:
            #             print('usuario no existe en tradegrecko')
            #             respuesta = tradegecko().createCompany(usuario.first_name+" "+usuario.last_name,"consumer",usuario.email, direccion.mobile)
            #             usuario.tradegecko_id = respuesta['company']['id']
            #             print(respuesta)
            #         else:
            #             try:
            #                 usuario.tradegecko_id = respuesta['companies'][0]['id']
            #             except KeyError as e:
            #                 capture_exception(e)
            #                 usuario.tradegecko_id = respuesta['company']['id']
            #         usuario.save()
            #     respuesta = tradegecko().createAddress(direccion.name, usuario.tradegecko_id,direccion.street,direccion.city,direccion.country, direccion.mobile, direccion.comuna, direccion.number)
            #     direccion.tradegecko_id = respuesta['address']['id']
            #     direccion.save()
            #     print('repuesta')
            # else:
            #     respuesta = tradegecko().createAddress(direccion.name, orden_actual.user.tradegecko_id,direccion.street,direccion.city,direccion.country, direccion.mobile, direccion.comuna, direccion.number)
            #     direccion.tradegecko_id = respuesta['address']['id']
            #     direccion.save()
            order_date = orden_actual.created_at.isoformat(timespec='milliseconds')
            # respuestatradegecko = tradegecko().createOrder(usuario.tradegecko_id,order_date,direccion.tradegecko_id,direccion.tradegecko_id,'finalized',items_tradegecko)
            # print(respuestatradegecko)
            # orden_actual.tradegecko_id = respuestatradegecko['order']['id']
        orden_actual.save()
        odoo_sync.delay(customer.id, orden_actual.order_number)
        print('terminado')
        return HttpResponse()

def botonIniciarSesion(request, emailo):
    try:
        usuario = User.objects.get(email=emailo)
    except User.DoesNotExist:
        return JsonResponse('Usuario no existe', safe=False)
    
    respuesta = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    expiracion = datetime.now() + timedelta(minutes=10)
    codigo = Logincodes.objects.create(user=usuario, code=respuesta, expiration_date=expiracion)
    cuerpo_email = 'https://api.kokorofoods.cl/inicio/'+usuario.email+'/'+respuesta
    fields = { "code": respuesta}
    mailclient = Omnisend().CustomeEvent("614e1eb0f5765e001ced48ae", "Login code", "Codelogin", usuario.email, fields )
    if mailclient.status_code == 204:
        return JsonResponse('Te enviamos un correo con el codigo', safe=False)
    else:
        return JsonResponse('error al enviar correo, por favor intentalo nuevamente', safe=False)
    
def logear(request,emailo,codigo):
    usuario = get_object_or_404(User, email=emailo)
    try:
        prueba = Logincodes.objects.get(user=usuario, code=codigo)
        if (prueba.expiration_date.timestamp() > datetime.now().timestamp()):
            return JsonResponse('Exito', safe=False)
        else:
            return JsonResponse('el codigo no es valido, por favor intente nuevamente', safe=False)
    except Logincodes.DoesNotExist:
        return JsonResponse('el codigo no es valido, por favor intente nuevamente', safe=False)

@csrf_exempt
def webhookTradegecko(request):
    respuesta = json.loads(request.body)
    orderitems = tradegecko().getOrder(respuesta['object_id'])['order']["order_line_item_ids"]
    for item in orderitems:
        lineitem = tradegecko().getOrderLineItem(item)
        cantidad = int(float(lineitem['order_line_item']['quantity']))
        if lineitem['order_line_item']['variant_id'] is None:
            continue        
        variant = tradegecko().getVariant(lineitem['order_line_item']['variant_id'])
        try:
            product = Product.objects.get(tradegecko_id=int(float(variant['variant']['product_id'])))
        except:
            continue
        product.quantity = product.quantity - cantidad
        product.save()
    return HttpResponse(status=200)

@csrf_exempt
def webhookTradegeckoStock(request):
    respuesta = json.loads(request.body)
    variant = tradegecko().getVariant(respuesta['object_id'])
    try:
        producto = Product.objects.get(tradegecko_id=variant['variant']['product_id'])
    except:
        return HttpResponse(status=500)   
    cantidad_de_producto =  int(variant['variant']["available_stock"]) + int(variant['variant']["production_incoming_stock"])
    if cantidad_de_producto >= 0:
        producto.quantity = cantidad_de_producto
        producto.save()
    return HttpResponse(status=200)

@csrf_exempt
def webhookTradegeckoDespacho(request):
    respuesta = json.loads(request.body)
    print('recibido webhook despacho tradegecko',respuesta)
    ordentradegecko = tradegecko().getOrder(respuesta['order_id'])
    print(ordentradegecko)
    try:
        orden_actual = Order.objects.get(tradegecko_id=respuesta['order_id'])
    except:
        return HttpResponse(status=500)
    orden_actual.status = 'Despachado'
    orden_actual.internal_status = 'Despachado'
    orden_actual.tracking_number = ordentradegecko['order']['tracking_number']
    orden_actual.carrier = "Starken"
    orden_actual.save()
    email = Omnisend().FullfilmentOrder(respuesta['order_id'], "Starken", "https://www.starken.cl/seguimiento", ordentradegecko['order']['tracking_number'])
    #{'object_id': 100052429, 'event': 'fulfillment.create', 'timestamp': 1630603604, 'resource_url': 'https://api.tradegecko.com/fulfillments/100052429.json', 'order_id': 138840206}
    return HttpResponse(status=200)


def mailtest(request):
    #liorenapp = Lioren()
    #mailclient = omnisend().addCustomer("example_store",'56',"bruno.fournies@gmail.com","Bruno","Fournies")
    #mailclient = omnisend().getOrder("example_store",'16023')
    #respuesta = omnisend().getAllProducts("example_store")#liorenapp.login()
    #respuesta = liorenapp.getBoleta(6)
    #print('claro',mailclient)
    #respuesta = omnisend().getAllProducts("store_yna2pgsxewc7gfds882z")
    #respuesta =  omnisend().getProduct("store_yna2pgsxewc7gfds882z","596972568627")["variants"][0]['id']
    #respuesta1 = tradegecko().getProduct(33391458)
    #respuesta = tradegecko().getVariant(respuesta1['product']['variant_ids'][0])
    #print(respuesta['variant']['available_stock'])
    #respuesta = tradegecko().updateVariantQuantity(respuesta1['product']['variant_ids'][0],int(respuesta['variant']['committed_stock'])+1)  
    #respuesta = respuesta = tradegecko().getCustomerbyEmail("cfournies@gmail.com")
    #usuario = User.objects.get(id=2)
    #print(usuario.first_name+" "+usuario.last_name,usuario.email)
    #respuesta = tradegecko().createCompany(usuario.first_name+" "+usuario.last_name,"consumer",str(usuario.email))
    respuesta = tradegecko().getOrder('138840206')
    #producto = Product.objects.all()
    #for i in producto:
    #    print(i.created_at,type(i.created_at),i.created_at.strftime("%Y-%m-%d"))
    #    break
    #print(respuesta['companies'],not respuesta['companies'])
    #respuesta = tradegecko().getProduct(33391458)
    #print(respuesta)
    #respuesta = omnisend().getStores()
    #respuesta = omnisend().addStore("kokorousa","Kokorofoods","USD")
    return JsonResponse(respuesta, safe=False)

def paymentRedirect(request):
    sleep(0.5)
    order_number = request.GET.get('order')
    order = Order.objects.get(order_number=order_number)
    if order.internal_status == 'Pago Confirmado':
        return redirect(settings.FRONT_URL + 'exito?order=' + order_number)
    else:
        return redirect(settings.FRONT_URL + 'rechazado?order=' + order_number)