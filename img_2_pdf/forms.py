from django import forms
from img_2_pdf.models import pdfImage
from django.forms import ClearableFileInput
class pdfImageUpload(forms.ModelForm):
    # imag=forms.ImageField(widget=forms.SelectMultiple)
    class Meta:
        model = pdfImage
        fields = ['imag']
        widgets={
            'imag': ClearableFileInput(attrs={'multiple': True})

        }