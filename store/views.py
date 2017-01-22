from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.filter(stock__gt=0).order_by('price')
    return render(request, 'store/item_list.html', {"items": items})