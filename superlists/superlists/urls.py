from django.conf.urls import include, url
from lists import views
            #regular expression: empty string
urlpatterns = [url(r'^$', views.home_page, name = 'home'),
url(r'^lists/the-only-list/$', views.view_list, name='view_list'),
]
