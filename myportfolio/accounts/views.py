from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') # has to click on sign up
    template_name = 'accounts/signup.html'

# def Mainpage(request):
#     return render(request,'accounts/accounts_index.html')
