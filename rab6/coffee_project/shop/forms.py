from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):

    class Meta:
        model = Coffee
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'uikit-input', 'placeholder': 'Введите название'}),
            'price': forms.NumberInput(attrs={'class': 'uikit-input', 'placeholder': 'Введите цену'}),
        }