from django.conf.urls import url
from . import views

urlpatterns = [
    # url expression /
    url(r'^$', views.index, name="index"),

    # url expression /
    url(r'^recipe/$', views.list, name="list"),

    # url expression /recipe/<recipe_id>/
    url(r'^recipe/(?P<recipe_id>[0-9]+)$', views.detail, name="detail"),

]