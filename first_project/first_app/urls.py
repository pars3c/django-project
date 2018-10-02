from django.conf.urls import url, include
from first_app import views

urlpatters = [
    url(r'^$', views.index, name='index'),
]