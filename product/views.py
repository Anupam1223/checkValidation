from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Product

# Create your views here.
class ProductAdd(TemplateView):
    template_name = "productadd.html"

    def post(self, request):
        product = Product()
        product.name = request.POST.get("name")
        product.quantity = request.POST.get("quantity")
        product.stock = request.POST.get("stock")
        product.price = request.POST.get("price")
        product.image = request.POST.get("image")
        product.save()

        return render(
            request,
            "productadd.html",
        )


class ProductView(TemplateView):
    template_name = "productread.html"

    def get(self, request):

        product = Product.objects.all()
        return render(request, self.template_name, {"product": product})
