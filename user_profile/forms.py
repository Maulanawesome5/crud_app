from django import forms


# Membuat form registrasi user
class Form_Register(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)

