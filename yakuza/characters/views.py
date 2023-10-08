from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "characters/index.html")

def kiryu(request):
    return HttpResponse("alo kiryu")

def majima(request):
    return HttpResponse("alo majima")