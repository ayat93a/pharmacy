from itertools import product
from .serializers import ProductSerializers
from pharm.models import Product
from rest_framework import generics


class ProductListCreateAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers 
