from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/login/$', views.login, name='login'),
    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    # # url(r'^accounts/register/$', views.login, name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^store/', include('store.urls')),
    url(r'', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)