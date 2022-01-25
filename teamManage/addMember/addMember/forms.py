from django import forms
from .models import Post

class addUserForm (forms.ModelForm):
	class Meta:
		model = Post
		fields = ('first', 'last', 'email', 'phone')