from .models import Value
from django.forms import ModelForm, NumberInput


class ValueForm(ModelForm):
    class Meta:
        model = Value
        fields = ['capacity', 'amplitude', 'duration', 'resistance', 'time']

        widgets = {
            "capacity": NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Введите емкость конденсатора'
            }),
            "amplitude": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите амплитуду'
            }),
            "duration": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите длительность импульса'
            }),
            "resistance": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сопротивление резистора'
            }),
            "time": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите шаг процесса'
            }),
        }