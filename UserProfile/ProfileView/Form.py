class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(
        validators=[validate_email], 
        widget=forms.EmailInput())
    password = forms.CharField(
        max_length=200, 
        widget=forms.PasswordInput(), 
        validators=[validate_password]
    )
    
    id_number = forms.CharField(max_length=20)
    occupation = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=100)
    street_number = forms.CharField(max_length=10)
    flat_number = forms.CharField(max_length=10, required=False)
    zip_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=10)