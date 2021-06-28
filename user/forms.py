from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.models import AbstractUser


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        error_messages = {
            "username": {"required": "please enter username"},
            "first_name": {"required": "please enter first name"},
            "last_name": {"required": "please enter last name"},
            "email": {"required": "please enter email"},
            "password": {"required": "please enter password"},
        }
        widgets = {
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter Password",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter Name",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter firstname",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter email",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter lastname",
                }
            ),
        }

    """
    name = forms.CharField(
        error_messages={"required": "please enter name"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name",
            }
        ),
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Address",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
            }
        )
    )

    image = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "custom-file-input",

                "placeholder": "Enter Name",
            }
        )
    )
    """

    def clean(self):
        cleaned_data = super().clean()

        valEmail = self.cleaned_data.get("email")

        verifyUser = User.objects.filter(email=valEmail).first()

        if not valEmail:
            return 0
        if verifyUser:
            raise forms.ValidationError("Email already exists!!!")
