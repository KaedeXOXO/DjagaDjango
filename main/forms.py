from .models import Hardware
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class HardwareForm(ModelForm):
    class Meta:
        model = Hardware
        fields = ['title', 'author', 'text', 'published', 'count']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholger': 'Введіть назву'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholger': 'Введіть виробника'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholger': 'Введіть опис'
            }),
            'published': TextInput(attrs={
                'class': 'col-xs-4',
                'id': 'ex1',
                'placeholger': 'Введіть рік випуску'
            }),
            'count': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholger': 'Введіть кількість'
            })
        }