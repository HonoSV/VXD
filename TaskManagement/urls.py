__author__ = 'v_htang'

from django.conf.urls import url, include
from django.contrib import admin
from TaskManagement import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^welcome-(?P<nid>\w+)/', views.welcome),
    url(r'^project_edit/', views.project_edit),
    url(r'^task_edit/', views.task_edit),
    url(r'^test_ajax/', views.test_ajax),
    url(r'^project-(?P<nid>\d+)/', views.project),
    url(r'^task_detail-(?P<nid>\d+)/', views.task_detail),
]