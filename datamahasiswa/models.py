from distutils.command.upload import upload
from django.db import models

# Create your models here.

class TabelMahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='mahasiswa/')
    
    def __str__(self):
        return self.nama