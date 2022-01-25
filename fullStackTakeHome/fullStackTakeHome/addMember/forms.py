from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    CHOICES=[(0,'Regular - cannot delete members'), (1,'Admin - can delete members')]
    role = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
    
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email', 'phone', 'role']

      