from django.conf.urls import url
import datetime as dt
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^profile$', views.user_profile, name='user-profile'),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^edit/profile$', views.edit_profile, name="edit-profile"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^newcomment/(\d+)/$', views.new_comment, name='new-comment'),
    url(r'^new/event$',views.new_event, name ='new-project'),
    
]