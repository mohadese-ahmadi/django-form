from django import forms
class registrationForm(forms.Form):
    firstName=forms.CharField()
    lastName=forms.CharField(required=False)
    password=forms.CharField(widget=forms.PasswordInput())