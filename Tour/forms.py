from django import forms

from .models import Users

class ChoiceForm(forms.Form):
    sample1 = forms.CharField()
    sample = forms.CharField()
    

class SignUpForm(forms.ModelForm):
	
	user_name = forms.CharField(max_length=50, label="Name")
	user_email = forms.EmailField(max_length=50, label="email")
	user_password = forms.CharField(widget=forms.PasswordInput(), label="Password")

	class Meta:
		model=Users
		fields = ['user_name','user_email','user_password']
		
