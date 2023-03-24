from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

app_name = 'user'

router = DefaultRouter()
router.register('account', views.AccountsViewSet)

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('', include(router.urls)),
]