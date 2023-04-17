from django.db import models

# EMPLOYMENT_CHOICES = (
#     ('Part-time'),
#     ('Full-time'),
#     ('Contract')
# )
CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Drug(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    employee_code = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=250)
   
    
    def __str__(self) -> str:
        return self.drug_name