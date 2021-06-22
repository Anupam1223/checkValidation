from django import forms
from .models import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "quantity", "stock", "price"]
        error_messages = {
            "name": {"required": "please enter product name"},
            "quantity": {"required": "please enter quantity"},
            "stock": {"required": "please enter stock"},
            "price": {"required": "please enter price"},
        }
        widgets = {
            "name": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter product name",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "please enter total quantity",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "please enter total stock",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "please enter price",
                }
            ),
        }

    """
    name = forms.CharField(
        error_messages={"required": "please enter name"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter product name",
            }
        ),
    )
    quantity = forms.IntegerField(
        error_messages={"required": "please enter name"},
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "please enter total quantity",
            }
        ),
    )
    stock = forms.IntegerField(
        error_messages={"required": "please enter total stock"},
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "please enter total stock",
            }
        ),
    )
    price = forms.IntegerField(
        error_messages={"required": "please enter price of product"},
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name",
            }
        ),
    )
    """
