from django.shortcuts import render
from .models import *
# Create your views here.

class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)

    def page(request, page_num=1):
        new_active_item = request.GET.get("new_active_item")
        if new_active_item is not None:
            active_item = Level.objects.filter(title = new_active_item)[0]




            unfolded_items = [active_item]

            while not active_item.is_menu:
                active_item = active_item.parent_level
                unfolded_items.append(active_item)

            pk_list = [i.pk for i in unfolded_items]
            unfolded_items = Level.objects.filter(pk__in=pk_list)

            ctx = {
            "unfolded_items":unfolded_items,
            }
            return render(request,'main.html',ctx)
        ctx = {"active_items":None,}
        return render(request,'main.html',ctx)
