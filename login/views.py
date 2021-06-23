from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import LoginForm
from user.models import User
from django.contrib.auth import logout

# Create your views here.
def loginUser(request):

    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():

            fname = loginForm.cleaned_data["email"]
            fremember = loginForm.cleaned_data["rememberMe"]
            print(fremember)
            user = User.objects.get(email=fname)

            # session created
            request.session["user"] = user.email

            # return response
            messages.success(request, "User Logged in successfully")
            response = HttpResponseRedirect("../user/")

            if fremember == "True":
                print("entered cookie")
                response.set_cookie("cookieusername", fname)
            else:
                print("cookie not set")

            return response

        else:
            print("invalid form")
    else:
        if request.COOKIES.get("cookieusername"):
            return HttpResponseRedirect("../user/")
        else:
            print("username cookie not set")

        loginForm = LoginForm()

    return render(request, "login.html", {"form": loginForm})


def ForgotPass(request):
    pass


def user_logout(request):
    response = HttpResponseRedirect("../")
    response.delete_cookie("cookieusername")
    logout(request)
    return response
