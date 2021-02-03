from django.conf.urls import url


urlpatterns=[
    url(r'^profile$', views.user_profile, name='user-profile'),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^edit/profile$', views.edit_profile, name="edit-profile"),
    url(r'^search/', views.search_results, name='search_results'),
    
]