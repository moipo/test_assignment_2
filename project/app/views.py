from django.shortcuts import render
from .models import *
# Create your views here.

class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)

    def page(request, page_num=1):
        new_active_item_id = request.GET.get("new_active_item_id")
        new_disabled_item_id = request.GET.get("new_disabled_item_id")

        previous_unfolded_items_id = []
        unfolded_items_id = request.GET.get("unfolded_items_id")
        if unfolded_items_id is not None:
            previous_unfolded_items_id = list(map(int,unfolded_items_id.split()))

        if new_active_item_id is not None:
            new_active_item_id = int(new_active_item_id)
            if new_active_item_id not in previous_unfolded_items_id:
                previous_unfolded_items_id.append(new_active_item_id)

            unfolded_items_id = " ".join([str(i) for i in previous_unfolded_items_id]) if previous_unfolded_items_id is not None else ""
            unfolded_items = Level.objects.filter(pk__in=previous_unfolded_items_id)

            ctx = {
            "unfolded_items":unfolded_items,
            "unfolded_items_id":unfolded_items_id,
            }
            return render(request,'main.html',ctx)
        elif new_disabled_item_id is not None:
            new_disabled_item_id = int(new_disabled_item_id)
            if new_disabled_item_id in previous_unfolded_items_id:
                previous_unfolded_items_id.remove(new_disabled_item_id)
            unfolded_items_id = " ".join([str(i) for i in previous_unfolded_items_id]) if previous_unfolded_items_id is not None else ""
            unfolded_items = Level.objects.filter(pk__in=previous_unfolded_items_id)
            ctx = {
            "unfolded_items":unfolded_items,
            "unfolded_items_id":unfolded_items_id,
            }
            return render(request,'main.html',ctx)
        else:
            return render(request,'main.html',{})
