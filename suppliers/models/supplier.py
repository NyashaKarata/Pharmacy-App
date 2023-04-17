from django.db import models


CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    
   
    
    def __str__(self) -> str:
        return self.name