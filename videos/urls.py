from django.conf.urls import url

from . import views

app_name = 'videos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<video_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^logout-view/$', views.logout_view, name='logout_view'),
]
