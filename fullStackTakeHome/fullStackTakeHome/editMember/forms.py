from django import forms
from .models import EditUsers
from django.utils.translation import gettext_lazy as _

class EditUserForm(forms.ModelForm):
    CHOICES=[(0,'Regular - cannot delete members'), (1,'Admin - can delete members')]
    role = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)

    class Meta:
        model = EditUsers
        fields = ['firstName', 'lastName', 'email', 'phone', 'role']
  