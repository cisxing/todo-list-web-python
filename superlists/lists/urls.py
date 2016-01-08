from django.conf.urls import include, url
from lists import views
#First one that matches will be selected
urlpatterns = [
    url(r'^new$', views.new_list, name = 'new_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),

]

#() is containment in regular expression to capture
