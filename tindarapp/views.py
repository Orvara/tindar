from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
# Create your views here.
def index(request):
    return render(request, 'tindarapp/index.html')

def AboutPage(request):
    return render(request, 'tindarapp/about.html')

def MyndirPage(request):
    return render(request, 'tindarapp/myndaalbum.html')

# Form for Pantanir.html
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something code
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    # else:
    #     form = form.FormName()

    return render(request,'tindarapp/pantanir.html',{'form':form})
