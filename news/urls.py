from django.conf.urls import url
from . import views 


#list of urls instance for our application.
urlpatterns=[
    url('^$',views.welcome, name='welcome'),
    url('^today/$',views.news_of_day, name='newsToday')
]

#url pattern that match the url today and 

