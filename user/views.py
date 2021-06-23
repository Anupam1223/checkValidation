from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User
from .forms import UserAddForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def UserAdd(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            useraddform = UserAddForm(request.POST)
            if useraddform.is_valid():

                useradded = useraddform.save(commit=False)
                useradded.save()
                """
                fname = useraddform.cleaned_data["name"]
                faddress = useraddform.cleaned_data["address"]
                femail = useraddform.cleaned_data["email"]
                fpassword = useraddform.cleaned_data["password"]
                useradd = User(
                    name=fname, address=faddress, email=femail, password=fpassword
                )
                useradd.save()
                """
            else:
                print("invalid form")
        else:
            useraddform = UserAddForm()
    else:
        return HttpResponseRedirect("../login/")

    return render(request, "useradd.html", {"form": useraddform})


class UserView(TemplateView):
    template_name = "userread.html"

    def get(self, request):

        user = User.objects.all()
        return render(request, self.template_name, {"user": user})


def ChangePass(request):

    if request.method == "POST":

        fpassword = request.POST.get("oldPass")
        password1 = request.POST.get("newPass1")
        password2 = request.POST.get("newPass2")

        if not password1:
            raise ValidationError("please enter NEW PASSWORD")
        if not password2:
            raise ValidationError("please re-enter NEW PASSWORD")

        semail = request.session["user"]
        verifyUser = User.objects.filter(email=semail).first()
        userid = verifyUser.id
        userpass = verifyUser.password

        if fpassword == userpass:
            if password1 == password2:

                User.objects.filter(id=userid).update(password=password2)
                messages.success(request, "password updated in successfully")
                return HttpResponseRedirect("../")
            else:
                raise ValidationError("re-entered pasword didnt matched ")
        else:
            raise ValidationError("old password didnt matched")
