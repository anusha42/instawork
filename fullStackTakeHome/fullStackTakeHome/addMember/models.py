from django.db import models

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=50)
    
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    #role = models.TypedChoiceField(choices=CHOICES, coerce = int, widget=forms.RadioSelect)
