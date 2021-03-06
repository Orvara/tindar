from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from tindarapp.forms import FormName
from .forms import FormName
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'tindarapp/index.html')

def AboutPage(request):
    return render(request, 'tindarapp/about.html')

def MyndirPage(request):
    return render(request, 'tindarapp/myndaalbum.html')

def thanks(request):
    return render(request, 'tindarapp/thanks.html')

def showform(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            form.save()
            # EMAIL
            EMAIL_HOST_USER = 'orvarand@gmail.com'
            subject = form.cleaned_data['subject']
            message = 'Nafn: ' + form.cleaned_data['name'] +'\nEmail: ' + form.cleaned_data['from_email']  + '\nTitill:' + form.cleaned_data['subject'] + '\nSkilaboð:' + form.cleaned_data['message']
            recepient = str(form['from_email'].value())
            send_mail(subject,message, recepient, [EMAIL_HOST_USER] , fail_silently = False)
            return render(request, 'tindarapp/thanks.html', {'form': form })
        # else:
        #     print('ERROR FORM INVALID')
        #     return render(request, 'tindarapp/pantanir.html')
    
    return render(request, 'tindarapp/pantanir.html', {'form': form })
