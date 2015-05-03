from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
	url(r'^admin', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="mypage.html")),
]

#if settings.DEBUG:
 #   import debug_toolbar
  #  urlpatterns += patterns('',
   #     url(r'^__debug__/', include(debug_toolbar.urls)),
    #)