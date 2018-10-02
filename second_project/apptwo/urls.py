from django.conf.urls import url, include
from apptwo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]