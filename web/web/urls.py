from django.conf.urls import include,url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index_redirect, name='index_redirect'),
    url(r'^crud/',include('crud.urls')),
    url(r'^admin/', admin.site.urls),
]
