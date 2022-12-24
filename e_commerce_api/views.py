from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,mixins,authentication
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


@api_view(['POST'])
def CreateProduct(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return redirect('/api/products/')


@api_view(['POST'])
def UpdateProduct(request,pk):
    products=Products.objects.get(id=pk)
    serializer=ProductSerializer(instance=products,data=request.data)
    if serializer.is_valid():
        serializer.save()
    print(serializer.data)
    return redirect('/api/products/')
   
        
    # return Response('item updated')





@api_view(["GET"])
def DeleteProduct(request,pk):
    product=Products.objects.get(id=pk)
    product.delete()
    return Response('items delete sucessfully')



class Viewallclass(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    authentication_classes= [authentication.SessionAuthentication ,authentication.TokenAuthentication]



View_allclass=Viewallclass.as_view()