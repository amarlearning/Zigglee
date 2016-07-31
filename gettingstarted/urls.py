from django.conf.urls import include, url
from django.contrib import admin

# admin.autodiscover()
import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', admin.site.urls),
    # url(r'^$', include('hello.urls')),
    # url(r'^db', include('hello.urls')),
]
