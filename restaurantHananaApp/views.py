from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit
# Create your views here.
def home(request):
    produits = Produit.objects.all()
    ctx={"produits":produits}
    return render(request,'base/index.html',ctx)
def pizza(request):

    return HttpResponse('Hello Pizza')