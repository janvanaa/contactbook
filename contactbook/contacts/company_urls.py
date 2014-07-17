from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
#Complany urls    
    url(r'^$', views.ContactCompanyListView.as_view(), name='company-list'),
    url(r'^new$', views.ContactCompanyCreateView.as_view(), name='company-new'),
    url(r'^(?P<pk>\d+)$', views.ContactCompanyDetailView.as_view(), name='company'),
    url(r'^edit/(?P<pk>\d+)$', views.ContactCompanyUpdateView.as_view(), name='company-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ContactCompanyDeleteView.as_view(), name='company-delete'),
)