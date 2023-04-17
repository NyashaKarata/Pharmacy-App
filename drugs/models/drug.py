from django.db import models


CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Drug(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True)
    date_supplied = models.DateField(max_length=255)
    price = models.DecimalField(max_digits=6, max_length=6, decimal_places=2)
    quantity =  models.IntegerField(max_length=5, null=True)
    expiry_date = models.DateField(max_length=255)
    strength = models.CharField(max_length=255)
    # supplier = models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE,blank=True)
    
   
    
    def __str__(self) -> str:
        return self.name