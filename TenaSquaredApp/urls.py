from django.urls import path

from TenaSquaredApp import views

app_name = "TenaSquaredApp"

urlpatterns = [
    path("", views.index, name = "index"),   
    path("customers/", views.customers, name = "customers"),  
    path("customers/sign_in/<int:customer_id>/", views.sign_in, name = "sign_in"),   
]