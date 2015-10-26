from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, drchrono. You're at the birthday app index.")

def handleEmail(request):
    return HttpResponse("Hello, drchrono. You're at the birthday app email handler. You shouldn't see this.")