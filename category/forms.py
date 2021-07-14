from django import forms
from .models import Category


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "vendor"]
        error_messages = {
            "name": {"required": "please enter category name"},
            "vendor": {"required": "please enter vendor name"},
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter category name",
                }
            ),
            "vendor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "please enter vendor name",
                }
            ),
        }

