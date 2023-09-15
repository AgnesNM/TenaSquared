from django.shortcuts import render

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

        return JsonResponse(json.loads(data), safe=False)
        

def sign_in(request, customer_id):
    
    try:

        # Use get_object_or_404 to retrieve the book or return 404 if not found

        customer = get_object_or_404(Customer, pk=customer_id)
      
        # Customize the data you want to return in the JSON response

        data = {

            'cust_name': customer.cust_name
        }

    except:

        print("Error: Customer not found")

    else:
           
        return JsonResponse(data)
