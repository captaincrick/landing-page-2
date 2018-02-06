from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('name','email','wechat','phone_number',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'姓名'}),
            'email':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Email'}),
            'wechat':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'微信'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'手机号'}),
            }
