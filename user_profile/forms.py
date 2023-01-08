from django import forms


# Membuat form registrasi user
class Form_Register(forms.Form):
    # Custom Variable
    GENDER = (("male", "Pria"), ("female", "Wanita"))
    YEARS = range(1970,2021,1)

    firstname = forms.CharField(max_length=100, label="Nama Depan", label_suffix='')
    lastname = forms.CharField(max_length=100, required=False, label="Nama Belakang", label_suffix='')
    birthdate = forms.DateField(
        label="Tanggal Lahir",
        label_suffix='',
        widget=forms.SelectDateWidget(years=YEARS)
    )
    gender = forms.ChoiceField(choices=GENDER, label="Jenis Kelamin", label_suffix='')
    city = forms.CharField(label="Kota", label_suffix='')
    zipcode = forms.CharField(max_length=5, label="Kode Pos", label_suffix='')
    email = forms.EmailField(required=True, label_suffix='')
    password_field = forms.CharField(
        min_length=8,
        label="Password",
        label_suffix='',
        widget=forms.PasswordInput()
    )

