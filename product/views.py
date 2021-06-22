from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Product
from .forms import ProductAddForm
from django.http import HttpResponseRedirect

# Create your views here.
def ProductAdd(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            productaddform = ProductAddForm(request.POST)
            if productaddform.is_valid():

                productadd = productaddform.save(commit=False)
                productadd.save()
                """
                fname = productaddform.cleaned_data["name"]
                fquantity = productaddform.cleaned_data["quantity"]
                fstock = productaddform.cleaned_data["stock"]
                fprice = productaddform.cleaned_data["price"]
                """

            else:
                print("invalid form")
        else:
            productaddform = ProductAddForm()
    else:
        return HttpResponseRedirect("../../login/")

    return render(request, "productadd.html", {"form": productaddform})


class ProductView(TemplateView):
    template_name = "productread.html"

    def get(self, request):

        product = Product.objects.all()
        return render(request, self.template_name, {"product": product})
