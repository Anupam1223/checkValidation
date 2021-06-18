from django import forms


class UserAddForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name",
            }
        )
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
    """
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
        valname = self.cleaned_data["name"]
        if len(valname) < 4:
            print("your name shouldnt be less than 5")
            raise forms.ValidationError("your name shouln't be less than 5")
