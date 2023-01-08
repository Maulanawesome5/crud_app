from django import forms


class Coba(forms.Form):
    
    # # Django Form data type
    # Required false artinya kolom boleh kosong
    # Required true artinya kolom tidak boleh kosong
    # Max_Length untuk mengatur banyaknya karakter di dalam input
    int_field = forms.IntegerField(required=False)
    dec_field = forms.DecimalField(required=False)
    float_field = forms.FloatField(required=True)
    bool_field = forms.BooleanField(required=True)
    char_field = forms.CharField(required=False, max_length=15)

    # # String Input
    email_field = forms.EmailField(required=True)
    regex_field = forms.RegexField(regex=r"(P?<test>)")
    slug_field = forms.SlugField()
    url_field = forms.URLField()
    ip_field = forms.GenericIPAddressField()

    # # Select input
    PILIHAN = (
        ("nilai1", "opsi1"),
        ("nilai2", "opsi2"),
        ("nilai3", "opsi3"),
    )
    option_field = forms.ChoiceField(choices=PILIHAN)
    null_bool_field = forms.NullBooleanField()

    # # Date time
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    duration_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()

