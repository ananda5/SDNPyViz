from django.conf.urls import patterns, include, url

from django.contrib import admin
from inventory.views import get_nodes

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SDNPyViz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^node/', include('inventory.urls', namespace='inventory')),
    )
