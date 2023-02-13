from django.contrib import admin
from .models import Produit, Categorie
# Register your models here.

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['categorie_fk','designation','prix','date_pub','img']

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=["designation"]
    

    
