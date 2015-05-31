from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, AuthenticationForm

#from customauth.models import Users
from .models import Users

class ChoiceForm(forms.Form):
	sample1 = forms.CharField()
	sample = forms.CharField()
	
class RegisterForm(UserCreationForm):
	"""A form for creating new users. Includes all the required
	fields, plus a repeated password."""
	
	user_first_name = forms.CharField(max_length=50, label="First Name")
	user_last_name = forms.CharField(max_length=50, label="Last Name")
	user_email = forms.EmailField(max_length=255, label="email")
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:
		model = Users
		fields = ('user_first_name', 'user_last_name', 'user_email',)

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

	
#class SignUpForm(forms.ModelForm):
#	
#	user_first_name = forms.CharField(max_length=50, label="First Name")
#	user_last_name = forms.CharField(max_length=50, label="Last Name")
#	user_email = forms.EmailField(max_length=50, label="email")
#	password = forms.CharField(widget=forms.PasswordInput(), label="Password")

#	class Meta:
#		model=Users
##		fields = '__all__'#['user_name','user_email','user_password']
#		exclude = ['last_login']
		
