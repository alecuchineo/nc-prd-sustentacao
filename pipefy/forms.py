from django import forms
from pipefy.models import PipesManutencao

class ReprocessamentoPipefy(forms.ModelForm):
    class Meta:
        model = PipesManutencao
        exclude={}
        widgets={
            "pipe": forms.Select(attrs={}),
            "processar_atrazados": forms.CheckboxInput(attrs={'class':'select-picker'})
        }





    