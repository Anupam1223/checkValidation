from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Category
from .forms import CategoryAddForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def CategoryAdd(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            categoryaddform = CategoryAddForm(request.POST)

            if categoryaddform.is_valid():

                categoryadd = categoryaddform.save(commit=False)
                categoryadd.save()
                messages.error(request, "product added sucessfully")
                return HttpResponseRedirect("/product/productread")
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


def delete_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        data.delete()
        messages.error(request, "category deleted sucessfully")
        return HttpResponseRedirect("/category/categoryread")


def update_category(request, id):
    if request.method == "POST":
        data = Category.objects.get(pk=id)
        fm = CategoryAddForm(request.POST, instance=data)
        if fm.is_valid():
            print("hello")
            fm.save()
            messages.error(request, "category updated sucessfully")
            return HttpResponseRedirect("/category/categoryread")
    data = Category.objects.get(pk=id)
    fm = CategoryAddForm(instance=data)

    return render(request, "updatecategory.html", {"forms": fm})
