from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'main'

router = DefaultRouter()
router.register('store', views.storeView) 
router.register('product', views.productView)
router.register('product_category', views.ProcategoryView)
router.register('image', views.imageView) 
router.register('slider', views.sliderView) 
router.register('blog', views.blogView) 
router.register('recipes', views.recipeView) 
router.register('category', views.categoryView) 
router.register('tag', views.tagView) 
router.register('contacto', views.contactformView) 
router.register('order', views.orderView) 
router.register('lineitem', views.lineitemView)
router.register('shipping', views.shippingView)
router.register('address', views.addressView)
router.register('tiendas', views.tiendasView)

urlpatterns = [
    path('', include(router.urls)),
    path('retornopayku',views.retornopayku, name='retornopayku'),   
    path('botonIniciarSesion/<str:emailo>',views.botonIniciarSesion, name='botonIniciarSesion'),     
    path('logear/<str:emailo>/<str:codigo>/',views.logear, name='logear'),
    path('mail',views.mailtest, name='mail'),
    path('recipe/<slug:url>/', views.RecetasApiView.as_view(), name="receta"),
    path('webhookTradegecko', views.webhookTradegecko, name='webhookTradegecko'),
    path('webhookTradegeckoStock', views.webhookTradegeckoStock, name='webhookTradegeckoStock'),
    path('webhookTradegeckoDespacho', views.webhookTradegeckoDespacho, name='webhookTradegeckoDespacho'),
    path('payment_red',views.paymentRedirect, name='paymentRedirect'),
]