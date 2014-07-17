from django.conf.urls import patterns, include, url

from django.contrib import admin
from contacts.views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contactbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/', include('contacts.person_urls')),
    url(r'^company/', include('contacts.company_urls')),
)