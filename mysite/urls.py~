from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                           # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                           # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                           # url(r'^admin/', include(admin.site.urls)),

                       #(r'^top/$', 'myapp.views.main')
                       url(r'^$', 'myapp.views.main'),
                       url(r'^mysite/myapp/$',        'myapp.views.read'  ),
                       url(r'^mysite/myapp/create/$', 'myapp.views.create'),
                       url(r'^mysite/myapp/update/$', 'myapp.views.update'),
                       url(r'^mysite/myapp/delete/$', 'myapp.views.delete'),
)

