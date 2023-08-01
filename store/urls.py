from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('pay/', views.pay, name="pay"),
    path('upi/', views.upi, name="upi"),
    path('successful/', views.successful, name="successful"),
    path('unsuccessful/', views.unsuccessful, name="unsuccessful"),
	
	path('update_item/',views.updateItem, name="update_item"),
    path('placed/',views.placed, name="placed"),
    path('process_order/',views.processOrder, name="update_item"),
]