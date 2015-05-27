from django import forms

from .models import Users

class ChoiceForm(forms.Form):
    sample1 = forms.CharField()
    sample = forms.CharField()
    

class SignUpForm(forms.ModelForm):
	class Meta:
		model=Users
		fields = ['user_name', 'user_email', 'user_password']
