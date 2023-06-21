from django import forms


class ReprocessamentoPipefy(forms.Form):
    phase = forms.CharField(
        label="Fase",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Informe a fase do motor"
            }
        )
    )

    url = forms.CharField(
        label="URL Webhook",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Url de entrada do projeto no ApiPass"
            }
        )
    )

    tempo_pausa = forms.IntegerField(
        label="Tempo de pausa (Minutos)",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Tempo de pausa em minutos"
            }
        )
    )


    