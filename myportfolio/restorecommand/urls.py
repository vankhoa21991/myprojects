from django.conf.urls import url

from . import views

app_name='restorecommand'

urlpatterns = [
    url(r'^$', views.index,name='resto_index'),
    url(r'^search/$', views.newRestaurants,name='search_res'),
    url(r'^(?P<restaurant_id>\d+)/delete/$', views.deleteRestaurants,name='delete_res'),
    url(r'^(?P<restaurant_id>\d+)/edit/$', views.editRestaurants,name='edit_res'),
    url(r'^add/$', views.addRestaurants,name='add_res'),
    url(r'^restaurants/$', views.showRestaurants,name='restaurants'),
]
