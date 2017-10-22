from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def Mainpage(request):
    return render(request,'main.html')
