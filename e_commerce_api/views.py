from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,mixins
from .models import Products
# from django.shortcuts import get_object_or_404

from .serializer import ProductSerializer
# Create your views here.

@api_view(["GET"])
def Showall(request):
    products=Products.objects.all()
    serializer=ProductSerializer(products,many=True)

    return Response(serializer.data)

@api_view(["GET"])
def Viewproduct(request,pk):
    products=Products.objects.get(id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)


@api_view(["POST"])
def CreateProduct(request):
    serializer=ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def UpdateProduct(request,pk):
    product=Products.objects.get(id=pk)
    serializer=ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





@api_view(["GET"])
def DeleteProduct(request,pk):
    product=Products.objects.get(id=pk)
    product.delete()
    return Response('items delete sucessfully')