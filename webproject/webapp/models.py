from django.db import models

# Create your models h
class Links(models.Model):

    def __str__(self):
        return self.stringname
    address=models.CharField(max_length=250,null=True,blank=True)
    stringname=models.CharField(max_length=250,null=True,blank=True)
