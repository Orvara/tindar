from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return render(request, 'tindarapp/index.html')

def AboutPage(request):
    return render(request, 'tindarapp/about.html')

def PantanirPage(request):
    return render(request, 'tindarapp/pantanir.html')
