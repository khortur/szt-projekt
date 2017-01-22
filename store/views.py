from django.shortcuts import render

def item_list(request):
    return render(request, 'store/item_list.html', {})