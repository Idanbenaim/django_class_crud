from django.db import models

# Create your models here.
class Students(models.Model):
   name = models.CharField(max_length=50,null=True,blank=True)
   age = models.IntegerField()
   image = models.ImageField(null=True,blank=True,default='/placeholder.png',upload_to='Posted_Images')

   def __str__(self):
          return self.name