from django.db import models

# EMPLOYMENT_CHOICES = (
#     ('Part-time'),
#     ('Full-time'),
#     ('Contract')
# )
GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    employee_code = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, null=True)
    personal_email = models.CharField(max_length=255)
    national_id = models.CharField(max_length=10, unique=True, null=True)
    work_email = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    
    #payroll information
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # payee = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    # other_tax = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    hours_worked = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    #work information
    bank = models.CharField(max_length=50, null=True)
    bank_account_name = models.CharField(max_length=255, null=True)
    bank_account_number = models.CharField(max_length=35, null=True)
    bank_branch = models.CharField(max_length=40, null=True)
    
    
    def __str__(self) -> str:
        return self.first_name