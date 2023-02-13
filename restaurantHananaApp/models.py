from django.db import models

# Create your models here.
class Categorie(models.Model):
    designation = models.CharField(max_length=120)
    def __str__(self):
        return self.designation

class Produit(models.Model):
    categorie_fk = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    designation = models.CharField(max_length=120)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    date_pub = models.DateField(auto_now=True)
    img=models.ImageField(upload_to='media', blank=True,null=True)

    class Meta:
        ordering=['date_pub']
    def __str__(self):
        return self.designation
    
