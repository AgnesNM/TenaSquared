from django.urls import path

from TenaSquaredApp import views

app_name = "TenaSquaredApp"

urlpatterns = [
    path("", views.index, name = "index"),   
    path("customers/", views.customers, name = "customers"),  
    path("customers/one_customer/<int:customer_id>/", views.one_customer, name = "one_customer"),   
    path("customers/sign_up/", views.sign_up, name = "sign_up"),
]