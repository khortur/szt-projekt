from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>[0-9]+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^purchase/(?P<pk>\d+)/remove/$', views.purchase_remove, name='purchase_remove'),
    url(r'^purchase/add/(?P<item_id>\d+)/(?P<amount>\d+)/$', views.purchase_add, name='purchase_add'),
    url(r'^cart/accept$', views.accept_cart, name='accept_cart'),
]