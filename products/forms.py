from django import forms
from .models import Product


class CreateProduct(forms.ModelForm):

    class Meta:
        model = Product

        fields = ['name', 'desc', 'price', 'release_date']

        name = forms.CharField(
            max_length=50,
            required=True,
            widget = forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Enter product name'
            })
        )

        desc = forms.CharField(
            required=True,
            widget = forms.Textarea(attrs= {
            'class': 'form-control',
            'placeholder': 'Enter product description'
            })
        )

        price = forms.FloatField(
            required=True,
            widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product price'
            })
        )

        release_date = forms.DateField(
            widget = forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter product release date'
            })
        )
