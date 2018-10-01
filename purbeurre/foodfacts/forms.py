from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=50,
        required=True
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        required=True
    )


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=50,
        required=True
    )
    """
        email = forms.EmailField(
        label="E-mail",
    )
    email_confirm = forms.EmailField(
        label="Confirmez votre email",
    ) """
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        required=True
    )
    password_confirm = forms.CharField(
        label="Confirmez votre mot de passe",
        widget=forms.PasswordInput,
        required=True
    )
