from django.db import models


# Create your models here.
class Platerak(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=100)
    deskripzioa = models.TextField()
    osagaia = models.CharField(max_length=100)
    prezioa = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.izena

