from django.conf.urls import url
from . import views

urlpatterns = [
    # url expression /
    url(r'^$', views.index, name="index"),

    # url expression /recipe/
    url(r'^recipe/$', views.list, name="list"),

    # url expression /about/
    url(r'^about/$', views.about, name="about"),

    # url expression /about/
    url(r'^contact/$', views.contact, name="contact"),

    # url expression /recipe/<recipe_id>/
    url(r'^recipe/(?P<recipe_id>[0-9]+)$', views.detail, name="detail"),

]