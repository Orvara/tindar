from django import forms
from django.core import validators
from django.forms import widgets
from .models import Posts

class FormName(forms.ModelForm):
    name = forms.CharField(
        max_length=80, label='', required='True',
            widget=forms.TextInput(
                attrs={

                    'placeholder': 'Nafn'
                }
            )
        )
    from_email = forms.EmailField(
        max_length=255, label='', required='True',
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Netfang'
                }
            )
        )

    subject = forms.CharField(
        max_length=255, label='', required='True',
            widget=forms.TextInput(
                attrs={

                    'placeholder': 'Titill'
                }
            )
        )
        # text = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder': 'Erindi',
            'class':'input-control',
        }
    ))

    class Meta:
        model= Posts
        fields= ["name", "from_email", "subject", "message"]

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("Make sure emails match!")
