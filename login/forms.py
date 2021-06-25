from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)

# class for login form
class LoginForm(forms.Form):

    email = forms.EmailField(
        error_messages={"required": "please enter Email"},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Email",
            }
        ),
    )

    password = forms.CharField(
        error_messages={"required": "please enter password"},
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter password",
            }
        ),
    )
    rememberMe = forms.CharField(
        widget=forms.CheckboxInput(
            attrs={
                "id": "rememberMe",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()

        valEmail = self.cleaned_data.get("email")
        valpassword = self.cleaned_data.get("password")

        verifyUser = User.objects.filter(email=valEmail).first()

        if not verifyUser:
            raise ValidationError("user doesnt exist")

        if not valEmail:
            return 0
        if not valpassword:
            return 0

        if not check_password(valpassword, verifyUser.password):
            raise ValidationError("username and  password didnt matched")


# different class for password change
class ChangePassForm(forms.Form):

    email = forms.EmailField(
        error_messages={"required": "please enter Email"},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Email",
            }
        ),
    )
