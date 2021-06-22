from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User
from .forms import UserAddForm
from django.http import HttpResponseRedirect

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
