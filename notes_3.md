# On Serialization Gotchas (without DRF)

from django.core import serializers

from . models import Customer

from django.http import JsonResponse

from django.http import HttpResponse

data = serializers.serialize("json", Customer.objects.all())

print(JsonResponse(json.loads(data), safe=False))

print(HttpResponse(data, content_type="application/json"))