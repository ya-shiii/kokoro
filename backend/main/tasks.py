from datetime import datetime
from difflib import ndiff
from pydoc import resolve
from celery import shared_task
from main.integrations.tradegecko import tradegecko
from main.integrations.mailchimp import mailchimp
from main.integrations.zoho import zohoc
from .models import Product, Image, User, Lineitem, Order
import json
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist



@shared_task
def odoo_sync(customer_id, order):
    print("in zoho sync task")
    customer = User.objects.get(id=customer_id)
    orden_actual = get_object_or_404(Order, order_number=order)
    itemline= Lineitem.objects.filter(order__id=orden_actual.id)
    zoho_ins = zohoc()
    name = customer.first_name + ' ' + customer.last_name
    direccion = orden_actual.address
    street = direccion.street + ' ' +  direccion.number
    payload_contact = {"contact_name":  name,
                        "company_name": name,
                        "contact_type": "customer",
                        "language_code": "es",
                        "payment_terms": 30,
                        "contact_persons": [
                                {
                                    "salutation": "Mr",
                                    "first_name": customer.first_name,
                                    "last_name": customer.last_name,
                                    "email": customer.email,
                                    "mobile": orden_actual.address.mobile,
                                    "is_primary_contact": True
                                }
                            ],
                        "custom_fields": [
                                        {
                                            "value": direccion.rut,
                                            "index": 1
                                        }
                                    ],
                        "shipping_address": { 
                                        "attention": "mr",
                                        "address": street,
                                        "street2": direccion.comuna,
                                        "city": direccion.city,
                                        "country": "Chile",
                        }
        }
    response = zoho_ins.createContact(payload_contact)
    print(response)
    if response["code"] == 0:
        customer.odoo_id = response["contact"]["contact_id"]
        customer.save()
    elif response["code"] == 3062: 
        payload_contact = {
                    "shipping_address": { 
                                        "attention": "mr",
                                        "address": street,
                                        "street2": direccion.comuna,
                                        "city": direccion.city,
                                        "country": "Chile",
                        },
                    "custom_fields": [
                                        {
                                            "value": direccion.rut,
                                            "index": 1
                                        }
                                    ],
        }
        response = zoho_ins.updateContact(payload_contact, customer.odoo_id)
        print(response)
    line_item_zoho = []
    for item in itemline:
        product_response = zoho_ins.get_Product(item.product.odoo_id)
        total = int(item.quantity) * int(float(item.product.price))
        order_item = {
                    "item_id": product_response["item"]["item_id"],
                    "name": product_response["item"]["name"],
                    "description": product_response["item"]["name"],
                    "rate": int(float(item.product.price)),
                    "quantity": int(item.quantity),
                    "unit": "qty",
                    "item_total": total,
                    "warehouse_id": 3164900000000079012
                    }
        line_item_zoho.append(order_item)
    if orden_actual.shipping_cost > 0:
        order_item = {
                        "name": "5 a 10 días habiles",
                        "description": "Despacho a domicilio",
                        "rate": orden_actual.shipping_cost,
                        "quantity": 1,
                        "unit": "qty",
                        "item_total": orden_actual.shipping_cost,
                        "warehouse_id": 3164900000000079012
                        }
        line_item_zoho.append(order_item)
    now = datetime.now()
    date_today = now.strftime("%Y-%m-%d")
    payload_order = {"customer_id":customer.odoo_id,
                     "date": date_today,
                     "pricebook_id": 3164900000000079029,
                     "line_items": line_item_zoho
                     }
    order_response = zoho_ins.createOrder(payload_order)
    orden_actual.odoo_id = order_response["salesorder"]["salesorder_id"]
    orden_actual.save()
    confirm_response = zoho_ins.confirmOrder(order_response["salesorder"]["salesorder_id"])
    package_line_item = []
    invoice_line_item = []
    for item in order_response["salesorder"]["line_items"]:
        line_invoice = {
                "item_id": item["item_id"],
                "rate": item["rate"],
                "quantity":item["quantity"],
                "salesorder_item_id": int(item["line_item_id"]),
                "item_total": item["item_total"],
                "description": item["description"]
        }
        if item["description"] != "Despacho a domicilio":
            package_line = {
                            "so_line_item_id": int(item["line_item_id"]),
                            "quantity": item["quantity"]
                        }
            package_line_item.append(package_line)
        invoice_line_item.append(line_invoice)
    number = str(order_response["salesorder"]["salesorder_number"].split('-')[1])
    payload_invoice = {
                    "customer_id" : customer.odoo_id,
                    "invoice_number": "INV-" +  number,
                    "date": date_today,
                    "payment_terms": 30,
                    "line_items": invoice_line_item,
    }
    invoice_response = zoho_ins.createInvoice(payload_invoice)
    print(invoice_response)
    confirm_inv_res = zoho_ins.confirmInvoice(invoice_response["invoice"]["invoice_id"])
    payload_payment = {
                    "customer_id": customer.odoo_id,
                    "payment_mode": "cash",
                    "amount": invoice_response["invoice"]["total"],
                    "date": invoice_response["invoice"]["date"],
                    "invoices": [
                            {
                                "invoice_id": invoice_response["invoice"]["invoice_id"],
                                "amount_applied": invoice_response["invoice"]["total"],
                                "tax_amount_withheld": 0
                            }
                            ],
        }
    payment_response = zoho_ins.createPayment(payload_payment)
    return "ok"

def zoho_orderSync(page):
    zoho_ins = zohoc()
    trade = tradegecko()
    order_list = trade.getOrderAll(page)
    Zoho_product = zoho_ins.getAllProduct()
    for order in order_list['orders']:
        #add customer
        print(order)
        trade_contact = trade.getCustomer(order["company_id"])
        if trade_contact["companies"][0]["company_type"] == "consumer":
            contact_tipe = "customer"
            contact_name = trade_contact["companies"][0]["name"]
            company_name = trade_contact["companies"][0]["name"]
            contact_persons = []
            for idx, contact in enumerate(trade_contact["companies"][0]["contact_ids"]):
                contact_info = trade.getContact(contact)
                print(idx)
                if idx == 0:
                    print('here')
                    contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                               "last_name": contact_info["contacts"][0]["last_name"],
                               "email": contact_info["contacts"][0]["email"],
                               "mobile": contact_info["contacts"][0]["phone_number"],
                               "is_primary_contact":  True
                    }
                    contact_persons.append(contact_dic)
                # else:
                #     contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                #                "last_name": contact_info["contacts"][0]["last_name"],
                #                "email": contact_info["contacts"][0]["email"],
                #                "mobile": contact_info["contacts"][0]["phone_number"]
                #     }
        elif trade_contact["companies"][0]["company_type"] == "business":
            contact_tipe = "customer"
            contact_persons = []
            for idx, contact in enumerate(trade_contact["companies"][0]["contact_ids"]):
                contact_info = trade.getContact(contact)
                if idx == 0:
                    contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                               "last_name": contact_info["contacts"][0]["last_name"],
                               "email": contact_info["contacts"][0]["email"],
                               "mobile": contact_info["contacts"][0]["phone_number"],
                               "is_primary_contact":  True
                    }
                else:
                    contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                               "last_name": contact_info["contacts"][0]["last_name"],
                               "email": contact_info["contacts"][0]["email"],
                               "mobile": contact_info["contacts"][0]["phone_number"]
                    }
                contact_persons.append(contact_dic)
            contact_name = trade_contact["companies"][0]["name"]
            company_name = trade_contact["companies"][0]["name"]
        elif trade_contact["companies"][0]["company_type"] == "supplier":
            contact_tipe = "vendor"
            contact_persons = []
            for idx, contact in enumerate(trade_contact["companies"][0]["contact_ids"]):
                contact_info = trade.getContact(contact)
                if idx == 0:
                    contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                               "last_name": contact_info["contacts"][0]["last_name"],
                               "email": contact_info["contacts"][0]["email"],
                               "mobile": contact_info["contacts"][0]["phone_number"],
                               "is_primary_contact":  True
                    }
                else:
                    contact_dic = {"first_name": contact_info["contacts"][0]["first_name"],
                               "last_name": contact_info["contacts"][0]["last_name"],
                               "email": contact_info["contacts"][0]["email"],
                               "mobile": contact_info["contacts"][0]["phone_number"]
                    }
                contact_persons.append(contact_dic)
        Address = trade.getAddress(trade_contact["companies"][0]["address_ids"][0])
        payload_contact = {"contact_name":trade_contact["companies"][0]["name"],
                           "company_name": trade_contact["companies"][0]["name"],
                           "contact_type": contact_tipe,
                           "language_code": "es",
                           "payment_terms": 30,
                           "contact_persons": contact_persons,
                           "shipping_address": { 
                                            "attention": "mr",
                                            "address": Address["addresses"][0]["address1"],
                                            "street2": Address["addresses"][0]["address2"],
                                            "city": Address["addresses"][0]["city"],
                                            "state": Address["addresses"][0]["state"],
                                            "country": Address["addresses"][0]["country"],
                           },
                            "custom_fields": [
                                        {
                                            "value": trade_contact["companies"][0]["tax_number"],
                                            "index": 1
                                        }
                                    ],
        }
        print('------payload ---------')
        print(payload_contact)
        response = zoho_ins.createContact(payload_contact)
        if response["code"] == 0 and trade_contact["companies"][0]["company_type"] == "consumer":
            try:
                customer = User.objects.get(tradegecko_id=trade_contact["companies"][0]["id"])
                customer.odoo_id = response["contact"]["contact_id"]
                customer.save()
            except  ObjectDoesNotExist: 
                print("not in database")
        print('-------Contact -------')
        print(response)
        #Create order
        line_item_zoho = []
        for item in order["order_line_item_ids"]:
            line_items = trade.getOrderLineItem(item)
            if line_items["order_line_item"]["line_type"] == "shipping":
                order_item = {
                                    "name": line_items["order_line_item"]["label"],
                                    "description": "Despacho a domicilio",
                                    "rate": int(float(line_items["order_line_item"]["price"])),
                                    "quantity": int(float(line_items["order_line_item"]["quantity"])),
                                    "unit": "qty",
                                    "item_total": 3800,
                                    "warehouse_id": 3164900000000079012
                                    }
                line_item_zoho.append(order_item)
            else:
                product_info = trade.getVariant(line_items["order_line_item"]["variant_id"])
                for zoho_item in Zoho_product["items"]:
                    if zoho_item["name"] == product_info["variant"]["product_name"]:
                        total = int(float(line_items["order_line_item"]["price"])) * int(float(line_items["order_line_item"]["quantity"]))
                        order_item = {
                                        "item_id": zoho_item["item_id"],
                                        "name": zoho_item["name"],
                                        "description": zoho_item["name"],
                                        "rate": int(float(line_items["order_line_item"]["price"])),
                                        "quantity": int(float(line_items["order_line_item"]["quantity"])),
                                        "unit": "qty",
                                        "item_total": total,
                                        "warehouse_id": 3164900000000079012
                                        }
                        line_item_zoho.append(order_item)
                        break
        if order["default_price_list_id"] == "wholesale":
            price_list = 3164900000000079035
        else:
            price_list = 3164900000000079029
        if response["code"] > 0:
            response = zoho_ins.getContactByName(trade_contact["companies"][0]["name"])
            customer_id = response["contacts"][0]["contact_id"]
            if trade_contact["companies"][0]["company_type"] == "consumer":
                try:
                    customer = User.objects.get(tradegecko_id=trade_contact["companies"][0]["id"])
                    customer.odoo_id = customer_id
                    customer.save()
                except  ObjectDoesNotExist: 
                    print("not in database")
        else:
            customer_id = response["contact"]["contact_id"]
        payload_order = {"customer_id": customer_id,
                        "date": order["issued_at"],
                        "pricebook_id": price_list,
                        "line_items": line_item_zoho
                     }
        order_response = zoho_ins.createOrder(payload_order)
        print("------ order --------")
        print(order_response)
        confirm_response = zoho_ins.confirmOrder(order_response["salesorder"]["salesorder_id"])
        print("------ confirm order--------")
        print(confirm_response)
        if order["invoice_status"] == "invoiced":
            for invoice in order["invoice_ids"]:
                data_inv = trade.getInvoice(invoice)
                invoice_line_item = []
                package_line_item = []
                for item in order_response["salesorder"]["line_items"]:
                    line_invoice = {
                                    "item_id": item["item_id"],
                                    "rate": item["rate"],
                                    "quantity":item["quantity"],
                                    "salesorder_item_id": int(item["line_item_id"]),
                                    "item_total": item["item_total"],
                                    "description": item["description"]
                    }
                    if item["description"] != "Despacho a domicilio":
                        package_line = {
                                        "so_line_item_id": int(item["line_item_id"]),
                                        "quantity": item["quantity"]
                                    }
                        package_line_item.append(package_line)
                    invoice_line_item.append(line_invoice)
                payload_invoice = {
                                "customer_id" : customer_id,
                                "date": data_inv["invoices"][0]["invoiced_at"],
                                "payment_terms": 30,
                                "line_items": invoice_line_item,
                }
                invoice_response = zoho_ins.createInvoice(payload_invoice)
                print("------ invoice --------")
                print(invoice_response)
                confirm_inv_res = zoho_ins.confirmInvoice(invoice_response["invoice"]["invoice_id"])
                print("------ confirm invoice --------") 
                print(confirm_inv_res)
        if order["payment_status"] == "paid":
            payload_payment = {
                        "customer_id": customer_id,
                        "payment_mode": "cash",
                        "amount": invoice_response["invoice"]["total"],
                        "date": invoice_response["invoice"]["date"],
                        "invoices": [
                                {
                                    "invoice_id": invoice_response["invoice"]["invoice_id"],
                                    "amount_applied": invoice_response["invoice"]["total"],
                                    "tax_amount_withheld": 0
                                }
                                ],
            }
            payment_response = zoho_ins.createPayment(payload_payment)
            print("------ payment --------")
            print(response)
        if order["packed_status"] == "packed":
            payload_package = {
                            "date": invoice_response["invoice"]["date"],
                            "package_number": order_response["salesorder"]["salesorder_number"],
                            "line_items": package_line_item,
            }
            package_response = zoho_ins.createPackage(payload_package, order_response["salesorder"]["salesorder_id"])
            if package_response["code"] ==  36117:
                payload_package = {
                            "date": order_response["salesorder"]["date"],
                            "package_number": order_response["salesorder"]["salesorder_number"],
                            "line_items": package_line_item,
                     }
                package_response = zoho_ins.createPackage(payload_package, order_response["salesorder"]["salesorder_id"])
            print("------ package --------") 
            print(payload_package)
            print(package_response)
        if order["fulfillment_status"] == "shipped":
            payload_shipment = {
                            "shipment_number": invoice_response["invoice"]["invoice_number"],
                            "date": invoice_response["invoice"]["date"],
                            "reference_number": order["tracking_number"],
                            "contact_persons": invoice_response["invoice"]["customer_id"],
                            "delivery_method": "Starken",
                            "tracking_number": order["tracking_number"],
                        }
            shipment_response = zoho_ins.createShipment(payload_shipment,package_response["package"]["package_id"], order_response["salesorder"]["salesorder_id"])
            print("------ Shippment --------") 
            print(shipment_response)


def zoho_ProductSync():
    zoho_ins = zohoc()
    trade = tradegecko()
    i = 1 
    while i < 3:
        trade_products = trade.getAllProduct(i)
        for item in trade_products['variants']:
            if item['manufacturable']:
                product_payload ={"item_type": "sales",
                                "product_type": "goods",
                                "name": item['product_name'],
                                "sku" : item['sku'],
                                "unit": "qty",
                                "initial_stock": item['stock_on_hand']
                                }
            else:
                product_payload ={"item_type": "purchases",
                                "product_type": "goods",
                                "name": item['product_name'],
                                "sku" : item['sku'],
                                "unit": "qty",
                                "initial_stock": item['stock_on_hand']
                                }
            response = zoho_ins.createProduct(product_payload)
            print(response)
            if response['code'] == 0:
                try:
                    product = Product.objects.get(tradegecko_id=item['product_id'])
                    print(product)
                    product.odoo_id = response['item']['item_id']
                    product.save()
                except Product.DoesNotExist as e:
                    print(e)
                    continue
        i += 1
       


@shared_task(name='sync_product_new')
def sync_product_new():
    trade = tradegecko()
    products_ko = trade.product("kokorofoods")
    products_ku = trade.product("Kümkare")
    for product in products_ko:
        product_check = Product.objects.filter(tradegecko_id=product['id']).count()
        if product_check == 0 and product['product_type'] == 'Producto final':
            variant_ids = product['variant_ids']
            variants_result = trade.variant(variant_ids)
            for variant in variants_result:
                if variant['manufacturable'] == True and product['product_type'] == 'Producto final':
                    varinat_info= variant
                    new_product = Product(name=product['name'],
                                        description=product['description'], quantity=varinat_info['committed_stock'],
                                        price=varinat_info['retail_price'], store_id=2, is_masvendido=False,
                                        is_destacado=False, tradegecko_id=product['id'], precio_comparacion=0)
                    if product['image_url'] != None:
                        new_image = Image(image_url=product['image_url'], product=new_product)
                    new_product.save()
                    new_image.save()
    for product in products_ku:
        product_check = Product.objects.filter(tradegecko_id=product['id']).count()
        if product_check == 0 and product['product_type'] == 'Producto final':
            variant_ids = product['variant_ids']
            variants_result = trade.variant(variant_ids)
            for variant in variants_result:
                if variant['manufacturable'] == True and product['product_type'] == 'Producto final':
                    varinat_info= variant
                    new_product = Product(name=product['name'],
                                        description=product['description'], quantity=varinat_info['committed_stock'],
                                        price=varinat_info['retail_price'], store_id=1, is_masvendido=False,
                                        is_destacado=False, tradegecko_id=product['id'], precio_comparacion=0)
                    if product['image_url'] != None:
                        new_image = Image(image_url=product['image_url'], product=new_product)
                    new_product.save()
                    new_image.save()

def mailchimpSync():
    Allproduct = Product.objects.filter(mailchimp_id = None)
    chimp = mailchimp()
    if len(Allproduct) > 0 :
        for product in Allproduct:
            payload = { "id":str(product.id),
                        "title":product.name,
                        "handle":"pasta-de-Ajo-Negro-y-Miel-de-Ulmo-140gr",
                        "url":"https://tienda.kokorofoods.com/products/pasta-de-ajo-negro-y-miel-de-ulmo-140gr",
                        "description":"<p>La miel de ulmo es reconocida a nivel mundial por su exquisito sabor, es producida en el Sur de Chile en la cordillera de los Andes, al mezclarla con el Ajo Negro ambos potencian su dulzor, suavidad y un sabor inigualable ideal para todo tipo de aperitivos y onces.</p>",
                        "type":"",
                        "vendor":"kokorofoods",
                        "image_url":"https://api.kokorofoods.cl/media/product_image/product_pasta_de_ajo_negro_y_miel_de_ulmo_140gr.png",
                        "variants":[],
                        "images":[],
                        "published_at_foreign":"2021-04-16T01:24:10+00:00"
                        }
            response = chimp.addProduct()