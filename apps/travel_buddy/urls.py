from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$', views.index),
    url(r'^travels/$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^travels/destination/(?P<trip_id>\d+)/$', views.showtrip),
    url(r'^travels/add/$', views.add),
    url(r'^create/$', views.create),
    url(r'^join/(?P<trip_id>\d+)/$', views.join),
    url(r'^delete/delete/$', views.delete_everything),
]