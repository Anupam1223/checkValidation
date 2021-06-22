from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path("", views.loginUser, name="login"),
    path("fortgotpass/", views.ForgotPass, name="fortgotpass"),
    path("logout/", views.user_logout, name="logout"),
]
