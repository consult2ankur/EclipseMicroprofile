from django.shortcuts import render,render_to_response
from rest_framework.generics import *
from rest_framework import generics,views,status
# from django.views.generic import CreateView
from .models import Account
from .serializer import AccountSerializer
from django.http import Http404,HttpResponse
from rest_framework import response 
from rest_framework.response import Response

class Account_create(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Account.objects.all()
    serializer_class=AccountSerializer
    def get(self, request):
        Accounts = Account.objects.all()
        serializer = AccountSerializer(Accounts)
        return response.Response(serializer.data)

    # def create():

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
class Account_update(views.APIView):
    # queryset = Account.objects.all()
    # serializer_class=AccountSerializer
    def get(self,request,pk):
        queryset = Account.objects.get(pk=pk)
        serializer_class=AccountSerializer(queryset)
        return Response(serializer_class.data)
    def update(self, request, pk, format=None):
        queryset = Account.objects.get(pk=pk)
        serializer = AccountSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Account_list(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class=AccountSerializer

class Account_remove(generics.DestroyAPIView):
    def get(self,request,pk):
        queryset = Account.objects.get(pk=pk)
        serializer_class=AccountSerializer(queryset)
        return Response(serializer_class.data)
    def delete(self, request, pk, format=None):
        Account = Account.objects.get(pk=pk)
        Account.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # def delete (self,request,id):
    #     queryset = Account.objects.filter(id=id)
    #     serializer_class=AccountSerializer(queryset)
    #     return Response(serializer_class.data)