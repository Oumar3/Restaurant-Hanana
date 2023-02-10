from django.urls import path
from . import views

app_name = "restaurantHananaApp"

urlpatterns = [
    path('',views.home,name="home"),
    path('pizza',views.home,name="pizza")
]