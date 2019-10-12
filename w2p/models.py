from django.db import models

# Create your models here.
class Wordfiles(models.Model):
    wfile=models.FileField(upload_to='files')
    fullname=models.CharField(max_length=200)
    img=models.ImageField(upload_to='files')