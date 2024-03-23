from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)
 name = models.CharField(max_length=200,null = True, blank = True)
 price = models.IntegerField(null = True)