from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    ctx={"title":"Restaurant Hanana "}
    return render(request,'base/index.html',ctx)
def pizza(request):
    return HttpResponse('Hello Pizza')