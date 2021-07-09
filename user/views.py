from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User
from .forms import UserAddForm, UserUpdateForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def UserAdd(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            useraddform = UserAddForm(
                data=(request.POST or None), files=(request.FILES or None)
            )
            if useraddform.is_valid():
                useradded = useraddform.save(commit=False)
                useradded.set_password(useradded.password)
                useradded.save()

                messages.success(request, "User added sucessfully")
                return HttpResponseRedirect("/user/userread")
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

    # when get request is requested by user than this method is runned
    def get(self, request):
        # select all the data from user to render in userview
        user = User.objects.all()
        # rendering the userview template to see them
        return render(request, self.template_name, {"users": user})


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

        print(userpass, fpassword)

        # checks whether the password given by user and actual password matches or not
        if check_password(fpassword, userpass):
            # checks whether the new password matches
            if password1 == password2:

                password_to_save = make_password(password2)
                # update the passowrd
                User.objects.filter(id=userid).update(password=password_to_save)
                # if updated than message is shown in the dashboard
                messages.success(request, "password updated successfully")
                return HttpResponseRedirect("/login/")

            else:
                messages.error(request, "reenter password didnt matched")
                return HttpResponseRedirect("../")
        else:
            messages.error(request, "old password didnt matched")
            return HttpResponseRedirect("../")


def UpdateUser(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        fm = UserUpdateForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request, "user updated sucessfully")
            return HttpResponseRedirect("/user/userread")
        else:
            print("invalid form")

    data = User.objects.get(pk=id)
    fm = UserUpdateForm(instance=data)

    return render(request, "updateuser.html", {"form": fm})


def DeleteUser(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
        messages.success(request, "user deleted")
        return HttpResponseRedirect("../../userread")

    return HttpResponseRedirect("../")


def UserRegister(request):

    if request.method == "POST":
        useraddform = UserAddForm(request.POST)

        if useraddform.is_valid():

            print("register validate")
            useradded = useraddform.save(commit=False)
            useradded.set_password(useradded.password)
            useradded.save()

            current_site = get_current_site(request)
            mail_subject = "Activate your account."
            message = render_to_string(
                "acc_active_email.html",
                {
                    "user": useradded,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(useradded.id)),
                    "token": account_activation_token.make_token(useradded),
                },
            )
            to_email = useraddform.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(request, "verification mail sent, please check mail")
            return redirect(reverse("login:login"))

        else:
            print("invalid form")
    else:
        useraddform = UserAddForm()

    return render(request, "register.html", {"form": useraddform})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Email verified")
        return redirect(reverse("login:login"))
    else:
        messages.error(request, "please provide valid email address")
        return redirect(reverse("login:login"))


def Profile(request, id):
    if request.method == "POST":
        datas = User.objects.get(pk=id)
        fm = UserProfileForm(
            data=(request.POST or None), files=(request.FILES or None), instance=datas
        )
        if fm.is_valid():
            fm.save()
        else:
            print("invalid form")

    datas = User.objects.get(pk=id)
    fm = UserProfileForm(instance=datas)

    return render(request, "profile.html", {"form": fm})
