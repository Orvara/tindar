from django import forms
from django.core import validators
from django.forms import widgets

class FormName(forms.Form):
    name = forms.CharField(
        max_length=80, label='', required='True',
            widget=forms.TextInput(
                attrs={

                    'placeholder': 'Nafn'
                }
            )
        )
    email = forms.EmailField(
        max_length=255, label='', required='True',
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Netfang'
                }
            )
        )
    verify_email = forms.EmailField(
        max_length=255, label='', required='True',
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Netfang aftur',
                }
            )
        )
        # text = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder': 'Erindi',
            'class':'input-control',
        }
    ))

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
