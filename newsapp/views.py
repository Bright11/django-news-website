from django.shortcuts import render
from django.views import View
from .models import Category,News
# Create your views here.

class index(View):
    def get(self, request):
        catenews=Category.objects.filter(category__isnull=False).distinct()[:3]
        newsslide=News.objects.all()
        latest=News.objects.order_by("created_at")[:2]
        constext={"title":"bright python news website","catenews":catenews,"latest":latest,"newsslide":newsslide}
        return render(request,"pages/index.html",constext)

    def post(self,request):
        pass