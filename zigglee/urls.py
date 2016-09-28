from django.conf.urls import url
from . import views

urlpatterns = [
    # url expression /
    url(r'^$', views.index, name="index"),

    # url expression /recipe/<recipe_id>/
    url(r'^recipe/(?P<recipe_id>[0-9]+)$', views.detail, name="detail"),

    # zigglee/static/zigglee/uploads/
    url(r'^zigglee/static/zigglee/uploads/(?P<image_name>[*]+)$', views.image, name="image"),
]