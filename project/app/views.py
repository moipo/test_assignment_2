from django.shortcuts import render
from .models import *
# Create your views here.

class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)

    def page(request, page_num=1):
        menues = Level.objects.filter(page = page_num)

        ctx = {
            "menues":menues,
        }
        return render(request,'main.html',ctx)
