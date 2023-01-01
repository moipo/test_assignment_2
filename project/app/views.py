from django.shortcuts import render
from .models import *
# Create your views here.

class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)

    def page(request, page_num=1):
        new_active_item = request.GET.get("new_active_item")
        print(request.GET)
        previous_unfolded_items = list(map(int,request.GET.get("unfolded_items").split()))
        if new_active_item is not None:
            active_item = Level.objects.filter(title = new_active_item)[0]




            unfolded_items = [active_item]

            while not active_item.is_menu:
                active_item = active_item.parent_level
                unfolded_items.append(active_item)

            pk_list = [i.pk for i in unfolded_items]
            unfolded_items = Level.objects.filter(pk__in=pk_list) | Level.objects.filter(id__in=previous_unfolded_items)
            unfolded_items_id = " ".join([str(i.id) for i in unfolded_items])
            ctx = {
            "unfolded_items":unfolded_items,
            "unfolded_items_id":unfolded_items_id,
            }
            return render(request,'main.html',ctx)
        ctx = {"unfolded_items":None,}
        return render(request,'main.html',ctx)
