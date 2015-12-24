from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teacher.views.home', name='home'),
    # url(r'^teacher/', include('teacher.foo.urls')),
    url(r'^start/$','person.views.login' ),
    url(r'^search/','person.views.search' ),
    url(r'^create/', 'person.views.create'),
    url(r'^fanhui/', 'person.views.fanhui'),
    url(r'^updata/', 'person.views.updata'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^register/', 'person.views.register'),
    
    url(r'^add_event/','person.views.add_event'),
    url(r'^search_event/','person.views.search_event'),
    url(r'^search_event1/','person.views.search_event1'),
    url(r'^search_information/','person.views.search_information'),
    url(r'^search_information1/','person.views.search_information1'),
    url(r'^order_teacher/','person.views.order_teacher'),
    url(r'^appoinment/','person.views.order'),
    url(r'^solve_order/','person.views.solve_order'),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
