from django import forms
from .models import Phones

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields =['first_name', 'last_name','phone_number_1','phone_number_2','email']
        

    class Meta:
        model =Phones
        fields =['first_name', 'last_name','phone_number_1','phone_number_2','email']