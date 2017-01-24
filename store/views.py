from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Purchase
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404


def item_list(request):
    # items = Item.objects.filter(stock__gt=0).order_by('price')
    items = Item.objects.order_by('price')
    return render(request, 'store/item_list.html', {"items": items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'store/item_detail.html', {'item': item})


@login_required
def item_new(request):
    if not request.user.is_superuser:
        raise Http404

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'store/item_edit.html', {'form': form})


@login_required
def item_edit(request, pk):
    if not request.user.is_superuser:
        raise Http404

    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'store/item_edit.html', {'form': form})


@staff_member_required
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')


@login_required
def cart(request):
    user = request.user
    purchases = Purchase.objects.filter(buyer_id__exact=user.id)
    return render(request, 'store/cart.html', {"purchases": purchases})


@login_required
def purchase_remove(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.delete()
    return redirect('cart')


@login_required
def purchase_add(request, item_id, amount):
    item = get_object_or_404(Item, pk=item_id)
    user = request.user
    purchases = Purchase.objects.filter(item_id__exact=item_id).filter(buyer_id__exact=user.id)
    purchase = Purchase(item=item, amount=amount, buyer=user)
    if (purchases.count() > 0):
        purchase = purchases.first()
        purchase.amount += int(amount)
        if (purchase.amount > item.stock):
            purchase.amount = item.stock
    purchase.save()
    return redirect('cart')


@login_required
def accept_cart(request):
    user = request.user
    purchases = Purchase.objects.filter(buyer_id__exact=user.id)
    for purchase in purchases:
        item = purchase.item
        item.stock -= purchase.amount
        if item.stock == 0:
            item.delete()
        else:
            item.save()
    return render(request, 'store/accept_cart.html', {})