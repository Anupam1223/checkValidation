from django import forms
from .models import User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "address",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "staff",
            "admin",
            "password",
        ]
        error_messages = {
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
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "enter Name",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "firstname",
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
