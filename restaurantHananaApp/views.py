from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    a = list(range(4))
    ctx={"title":"Restaurant Hanana ","a":a}
    
    return render(request,'base/index.html',ctx)
def pizza(request):
    return HttpResponse('Hello Pizza')