from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    #Person urls
    url(r'^$', views.ContactPersonListView.as_view(), name='person-list'),
    url(r'^new$', views.ContactPersonCreateView.as_view(), name='person-new'),
    url(r'^(?P<pk>\d+)$', views.ContactPersonDetailView.as_view(), name='person'),
    url(r'^edit/(?P<pk>\d+)$', views.ContactPersonUpdateView.as_view(), name='person-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ContactPersonDeleteView.as_view(), name='person-delete'),
)    