from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create_user(request):
    return HttpResponse("Create_user")

def read_user(request):
    return HttpResponse("Read_user")

def update_user(request):
    return HttpResponse("Update_user")

def delete_user(request):
    return HttpResponse("Delete_user")