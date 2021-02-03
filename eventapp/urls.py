from django.conf.urls import url


urlpatterns=[
    url(r'^profile$', views.user_profile, name='user-profile'),
    
]