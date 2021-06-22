from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Category
from .forms import CategoryAddForm
from django.http import HttpResponseRedirect

# Create your views here.
def CategoryAdd(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            categoryaddform = CategoryAddForm(request.POST)

            if categoryaddform.is_valid():

                categoryadd = categoryaddform.save(commit=False)
                categoryadd.save()

                """
                fcategory = categoryaddform.cleaned_data["name"]
                fvendor = categoryaddform.cleaned_data["vendor"]
                """
            else:
                print("invalid form")
        else:
            categoryaddform = CategoryAddForm()
    else:
        return HttpResponseRedirect("../../login/")

    return render(request, "categoryadd.html", {"form": categoryaddform})


class CategoryView(TemplateView):
    template_name = "categoryread.html"

    def get(self, request):

        category = Category.objects.all()
        return render(request, self.template_name, {"category": category})
