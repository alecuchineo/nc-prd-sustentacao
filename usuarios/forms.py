from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Usuario",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Usuário"
            }
        )
    )
    senha= forms.CharField(
        label="Informe sua senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Senha",
            }
        )
    )


