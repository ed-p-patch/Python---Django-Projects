from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses/$', views.index),
    url(r'^courses/add/$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)/$', views.show_delete),
    url(r'^courses/del/(?P<id>\d+)$', views.delete_item),
]