from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^add/$', views.add),
    url(r'^create/$', views.create),
    url(r'^home/user/()/$', views.user_page),
    url(r'^books/(?P<book_id>\d+)/$', views.show_book)
]