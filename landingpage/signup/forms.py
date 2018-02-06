from django import forms
from .models import SignUp
from django.core import validators
from django.core.validators import validate_email


class SignUpForm(forms.ModelForm):

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = SignUp
        fields = ('name','email','phone_number',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Full Name'}),
            'email':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Phone Number'}),

            }
