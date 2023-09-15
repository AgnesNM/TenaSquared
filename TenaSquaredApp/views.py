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
        


