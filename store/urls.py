from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.item_detail, name='item_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)