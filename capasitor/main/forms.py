from .models import Value
from django.forms import ModelForm, NumberInput


class ValueForm(ModelForm):
    class Meta:
        model = Value
        fields = ['capacity', 'amplitude', 'frequency']

        widgets = {
            "capacity": NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Введите емкость'
            }),
            "amplitude": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите амплитуду'
            }),
            "frequency": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите частоту'
            })
        }