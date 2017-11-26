from django.conf.urls import url

from . import views

app_name='interview'

urlpatterns = [
    url(r'^$', views.index,name='interview_index'),
    url(r'^add/$', views.addQuestion,name='interview_add'),
    url(r'^all/$', views.allQuestion,name='interview_all'),
    url(r'^test/$', views.testQuestion,name='interview_test'),
    url(r'^(?P<question_id>\d+)/next/$', views.nextQuestion,name='interview_next'),
    url(r'^(?P<question_id>\d+)/delete/$', views.deleteQuestion,name='interview_delete'),
    url(r'^(?P<question_id>\d+)/edit/$', views.editQuestion,name='interview_edit'),
]
