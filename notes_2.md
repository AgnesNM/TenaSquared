from . models import Customer 

# Serializing data in Django

It's basically coverting your response data into a more usable format like json or xml


# a high level way to serialize data in django

from django.core import serializers


serializers.serialize("json", Customer.objects.all())

# Using a serializer object directly

json_serializer = serializers.get_serializer("json")

data_serializer = json_serializer()

data_serializer.serialize(Customer.objects.all())

serialized_data = data_serializer.getvalue()

    
# saving the formatted data in a file

with open("file.json", "w") as out:
    data_serializer.serialize(Customer.objects.all(), stream = out)

