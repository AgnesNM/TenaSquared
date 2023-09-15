from django.urls import path

from TenaSquaredApp import views

app_name = "TenaSquaredApp"

urlpatterns = [
    path("", views.index, name = "index"),   
    path("customers/", views.customers, name = "customers"),    
]