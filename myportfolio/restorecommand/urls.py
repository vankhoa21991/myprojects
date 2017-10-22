from django.conf.urls import url

from . import views

app_name='restorecommand'

urlpatterns = [
    url(r'^$', views.index,name='resto_index'),
]
