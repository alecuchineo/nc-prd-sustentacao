from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Usuario",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Usuário"
            }
        )
    )
    senha= forms.CharField(
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Senha"
            }
        )
    )