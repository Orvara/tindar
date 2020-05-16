from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from tindarapp.forms import FormName
from .forms import FormName
# Create your views here.
def index(request):
    return render(request, 'tindarapp/index.html')

def AboutPage(request):
    return render(request, 'tindarapp/about.html')

def MyndirPage(request):
    return render(request, 'tindarapp/myndaalbum.html')

# Form for Pantanir.html
# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             # Do something code
#             print("VALIDATION SUCCESS!")
#             print("NAME: "+form.cleaned_data['name'])
#             print("EMAIL: "+form.cleaned_data['email'])
#             print("TEXT: "+form.cleaned_data['text'])
#     # else:
#     #     form = form.FormName()
#
#     return render(request,'tindarapp/pantanir.html',{'form':form})
#
# Trying to send email - doesn't work atm
# def form_name_view(request):
#     if request.method == 'GET':
#         form = FormName()
#     else:
#         form = FormName(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             headers = form.cleaned_data['subject']
#             try:
#                 send_mail(subject, message, from_email, ['orvand@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('takk')
#     return render(request, "tindarapp/pantanir.html", {'form': form})
#
def thanks(request):
    return render(request, 'tindarapp/thanks.html')

def showform(request):
    form= FormName(request.POST or None)
    if form.is_valid():
        form.save()


    # EMAIL
        EMAIL_HOST_USER = 'orvarand@gmail.com'
        subject = form.cleaned_data['subject']
        message = 'Nafn: ' + form.cleaned_data['name'] +'\nEmail: ' + form.cleaned_data['from_email']  + '\nTitill:' + form.cleaned_data['subject'] + '\nSkilaboð:' + form.cleaned_data['message']
        recepient = str(form['from_email'].value())
        send_mail(subject,message, recepient, [EMAIL_HOST_USER] , fail_silently = False)
    # else:
    #     return render(request, 'tindarapp/pantanir.html')
    context= {'form': form }
    return render(request, 'tindarapp/thanks.html', context)
