from django.conf.urls import include, url
from lists import views
#First one that matches will be selected
urlpatterns = [
    url(r'^$', views.home_page, name = 'home'),
    url(r'^lists/new$', views.new_list, name = 'new_list'),
    url(r'^lists/the-only-list/$', views.view_list, name='view_list'),

]
