from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import logout
from .forms import ChangePassForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from user.models import User as users

# Create your views here
# ------------------ Views for logging in --------------------------
def loginUser(request):

    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():

            fname = loginForm.cleaned_data["email"]
            fremember = loginForm.cleaned_data["rememberMe"]
            print(fremember)
            user = users.objects.get(email=fname)

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


# ------------------ function for changing password --------------------------
def ForgotPass(request):

    if request.method == "POST":

        loginForm = ChangePassForm(request.POST)
        if loginForm.is_valid():

            fname = loginForm.cleaned_data["email"]
            associated_users = users.objects.filter(email=fname)

            print("hiii i am associated_users", associated_users, fname)

            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "resetPass/password_reset_email.txt"
                    print(email_template_name)
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "anupam.siwakoti@gmail.com",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("../../password_reset/done/")
        else:
            print("invalid form")
    else:
        loginForm = ChangePassForm()
    return render(request, "resetPass/forgotPass.html", {"form": loginForm})


# ------------------ function for logout --------------------------
def user_logout(request):
    response = HttpResponseRedirect("../")
    response.delete_cookie("cookieusername")
    logout(request)
    return response
