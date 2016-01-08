from django.conf.urls import include, url
from lists import views
#First one that matches will be selected
urlpatterns = [
    url(r'^$', views.home_page, name = 'home'),
    url(r'^lists/new$', views.new_list, name = 'new_list'),
    url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),

]

#() is containment in regular expression to capture
