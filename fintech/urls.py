from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='buy-item'),
    path('item/<int:id>/', views.item_detail, name='item-detail'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('create-payment-intent/<int:order_id>/', views.create_payment_intent, name='create_payment_intent'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('', views.home, name='home')
]

