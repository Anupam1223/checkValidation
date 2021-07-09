from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

# url name for users url, this will help us to easily find url
app_name = "user"

# path for user related work, when we access 'url:useradd' than the control of
# website will enter UserAdd view similarly with other urls
urlpatterns = [
    path("", views.UserAdd, name="useradd"),
    path("userread/", views.UserView.as_view(), name="userread"),
    path("changePass/", views.ChangePass, name="changepass"),
    path("<int:id>/", views.UpdateUser, name="updateuser"),
    path("deleteuser/<int:id>/", views.DeleteUser, name="deleteuser"),
    path("register/", views.UserRegister, name="register"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("profile/<int:id>/", views.Profile, name="profile"),
]
