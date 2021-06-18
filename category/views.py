from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Category

# Create your views here.
class CategoryAdd(TemplateView):
    template_name = "categoryadd.html"

    def post(self, request):
        category = Category()
        category.name = request.POST.get("name")
        category.vendor = request.POST.get("vendor")
        category.save()

        return render(
            request,
            "categoryadd.html",
        )


class CategoryView(TemplateView):
    template_name = "categoryread.html"

    def get(self, request):

        category = Category.objects.all()
        return render(request, self.template_name, {"category": category})
