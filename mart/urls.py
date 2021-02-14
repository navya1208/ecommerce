from . import views
from django.urls import path
from django.conf.urls import  url


urlpatterns = [
    path('',views.mart,name="mart"),
    path('cart/',views.cart,name="cart"),
    path('check/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),


]
