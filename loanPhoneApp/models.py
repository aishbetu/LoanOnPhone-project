from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class loanModel(models.Model):
    Name =          models.CharField(max_length=50, blank=False)
    phone_regex =   RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number =  models.CharField(validators=[phone_regex], max_length=17, null=False, unique=True)  # validators should be a list
    identity_no =   models.IntegerField(null=False, unique=True)
    Address =       models.CharField(max_length=300 , blank=False)
    reason =        models.TextField(blank=False)
    created_at =       models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name