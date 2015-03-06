# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', '{{project_name}}.views.hello',),
    # url(r'^(app_name)/hello/$', '(app_name).views.hello',),
)
