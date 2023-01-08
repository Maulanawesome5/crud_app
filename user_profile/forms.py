from django import forms


# Membuat form registrasi user
class Form_Register(forms.Form):
    # Custom Variable
    GENDER = (("male", "Pria"), ("female", "Wanita"))
    YEARS = range(1970,2021,1)

    firstname = forms.CharField(max_length=100, label="Nama Depan")
    lastname = forms.CharField(max_length=100, required=False, label="Nama Belakang")
    birthdate = forms.DateField(
        label="Tanggal Lahir",
        widget=forms.SelectDateWidget(years=YEARS)
    )
    gender = forms.ChoiceField(choices=GENDER, label="Jenis Kelamin")
    city = forms.CharField(label="Kota")
    zipcode = forms.CharField(max_length=5, label="Kode Pos")
    email = forms.EmailField(required=True)
    password_field = forms

