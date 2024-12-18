from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RecuperarSenhaForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget = forms.EmailInput(  
            attrs={
                'id':'input_recover_password',
                'class':'email_input_recover_password w-50 form-control',
                'placeholder':'email@com.br'
            }
        )
    )



class RegisterUserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(
            attrs={
                    "class": "form-control",
                    "placeholder": "Confirmar Senha"
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }

        help_texts = {
            'username':
            '''
                Apenas letras, números e @/./+/-/_ são permitidos no campo, com até 150 caracteres.
            '''
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Usuário"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "E-mail"
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Senha"
                }
            )
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        exist_username = User.objects.filter(username=username).exists()
        if exist_username:
            raise ValidationError(
                'Já existe um usuário com este username!'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exist_email = User.objects.filter(email=email).exists()
        if exist_email:
            raise ValidationError(
                'Já existe um usuário com este email!'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError({
                'password': 'Senha e a confirmação de senha precisam ser iguais'
            })


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'caixa-login',
                'class': 'form-control',
                'placeholder': 'Usuário'
            }
        )
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        ),
        required=True
    )