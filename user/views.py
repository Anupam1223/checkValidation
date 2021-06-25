from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
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

                password = useraddform.cleaned_data["password"]
                useradded.set_password(useradded.password)
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


# Create UserView to see user value
class UserView(TemplateView):
    # this view will render userread template
    template_name = "userread.html"

    #
    def get(self, request):
        #
        user = User.objects.all()
        #
        return render(request, self.template_name, {"user": user})


# ChangePass view will take in the request body with old and new password
def ChangePass(request):

    if request.method == "POST":

        fpassword = request.POST.get("oldPass")

        password1 = request.POST.get("newPass1")

        password2 = request.POST.get("newPass2")

        # if user submit empty old password then the program will raise validation error
        if not fpassword:
            raise ValidationError("please enter OLD PASSWORD")

        # if user submit empty new password then the program will raise validation error
        if not password1:
            raise ValidationError("please enter NEW PASSWORD")

        # if user submit empty new re-password then the program will raise validation error
        if not password2:
            raise ValidationError("please re-enter NEW PASSWORD")

        # extract session value to extract the user password from database
        semail = request.session["user"]

        # extract the user with matching email taken from session
        verifyUser = User.objects.filter(email=semail).first()

        # userid of extracted user
        userid = verifyUser.id

        # password of extracted pasword
        userpass = verifyUser.password

        # checks whether the password given by user and actual password matches or not
        if fpassword == userpass:
            # checks whether the new password matches
            if password1 == password2:
                # update the passowrd
                User.objects.filter(id=userid).update(password=password2)
                # if updated than message is shown in the dashboard
                messages.success(request, "password updated in successfully")
                # redirects to the dashboard
                return HttpResponseRedirect("../")
            else:
                raise ValidationError("re-entered pasword didnt matched ")
        else:
            raise ValidationError("old password didnt matched")
