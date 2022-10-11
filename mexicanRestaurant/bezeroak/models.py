from django.db import models

# Create your models here.
class Bezeroak(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=100)
    dni = models.CharField(max_length=9)
    kontaktuko_telefono_zenbakia = models.CharField(max_length=9)
    saldo = models.TextField()

    def __str__(self):
        return '%s' % self.izena