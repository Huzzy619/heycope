from django.db import models

# Create your models here.


class Hope(models.Model):
    email = models.EmailField( max_length=254)