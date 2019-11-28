from django import forms
from website.models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [
            'nome',
            'placa',
            'modelo',
        ]