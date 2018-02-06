from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import SignUp
from .forms import SignUpForm


class SuccessView(TemplateView):
    template_name = 'signup_kr/success.html'

class SignUpView(CreateView):
    model = SignUp
    form_class = SignUpForm

# Create your views here.
