from django.contrib import admin
from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
    path("categoryadd/", views.CategoryAdd, name="categoryadd"),
    path("categoryread/", views.CategoryView.as_view(), name="categoryread"),
]
