"""budget_xp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import *
from categories.views import *
from categories import urls as categories_url

urlpatterns = [
    # Categories pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$', 'subscribers.views.subscriber_new', name='sub_new'),

    # Admin pages
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^categories/', include(categories_url)),
    url(r'^categories/About/', categories_about, name='about'),
    url(r'^categories/$', categories_main_page),
    url(r'^categories/Tout$', categories_page),
    url(r'^categories/(\w+)/$', categories_children_page),
#    url(r'^contact-us/(?P<lang>[\w-]+)/$', ContactUs.as_view())


]
