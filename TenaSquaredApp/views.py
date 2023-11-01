# Create your views here.

from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from . models import Customer 


# Create your views here.

def index(request):

    return HttpResponse("Hey, let's create APIs in Django")


def customers(request):

    try:
    
        data = serializers.serialize("json", Customer.objects.all())         
        
    except:
        
        # This will check for any exception and then execute this print statement

        print("Error: Could not find customers")

    else:

        # return HttpResponse(data, content_type="application/json")

        return JsonResponse(json.loads(data), safe=False)
        

def one_customer(request, customer_id):
    
    try:

        # Use get_object_or_404 to retrieve the customer or return 404 if not found

        customer = get_object_or_404(Customer, pk=customer_id)
      
        # Customize the data you want to return in the JSON response

        data = {

            'cust_name': customer.cust_name
        }

    except:

        print("Error: Customer not found")

    else:
           
        return JsonResponse(data)
    

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def sign_up(request):
    
    try:

        new = Customer(cust_name="Abby", password="12345678")

        new.save()

    except:

        print("Customer not created")

    else:
           
        return HttpResponse("Customer successfully created")
