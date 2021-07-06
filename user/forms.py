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
                    "class": "form-control password",
                    "placeholder": "password",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "address",
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
                    "placeholder": "email",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "lastname",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        first_name = self.cleaned_data.get("first_name", None)
        if not first_name:
            raise forms.ValidationError("please provide firstname", code="invalid")

        last_name = self.cleaned_data.get("last_name", None)
        if not last_name:
            raise forms.ValidationError("please provide lastname", code="invalid")

        email = self.cleaned_data.get("email", None)
        if not email:
            raise forms.ValidationError("please provide email", code="invalid")

        # check whether mail already exists or not
        verifyUser = User.objects.filter(email=email).first()
        if verifyUser:
            raise forms.ValidationError("Email already exists!!!", code="invalid")

        address = self.cleaned_data.get("address", None)
        if not address:
            raise forms.ValidationError("please provide address", code="invalid")


class UserUpdateForm(forms.ModelForm):
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
        ]
        error_messages = {
            "address": {"required": "please enter your address"},
            "first_name": {"required": "please enter first name"},
            "last_name": {"required": "please enter last name"},
            "email": {"required": "please enter email"},
        }
        widgets = {
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "address",
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
                    "placeholder": "email",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "lastname",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        first_name = self.cleaned_data.get("first_name", None)
        last_name = self.cleaned_data.get("last_name", None)
        email = self.cleaned_data.get("email", None)
        address = self.cleaned_data.get("address", None)

        if not first_name:
            print("please provide firstname")
            raise forms.ValidationError("please provide firstname", code="invalid")

        if not last_name:
            print("please provide lastname")
            raise forms.ValidationError("please provide lastname", code="invalid")

        if not email:
            print("please provide email")
            raise forms.ValidationError("please provide email", code="invalid")

        if not address:
            print("please provide address")
            raise forms.ValidationError("please provide address", code="invalid")
