from django.db import models

# EMPLOYMENT_CHOICES = (
#     ('Part-time'),
#     ('Full-time'),
#     ('Contract')
# )

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    employee_code = models.CharField(max_length=255)
    personal_email = models.CharField(max_length=255)
    work_email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    #Add pay details
    
    
    def __str__(self) -> str:
        return self.first_name