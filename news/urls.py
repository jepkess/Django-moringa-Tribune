from django.conf.urls import url
from . import views 
from django.urls import path


#list of urls instance for our application.
urlpatterns=[
   
    path('',views.news_today, name='newsToday'), #urlpattern for the new_of_ day view function.
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news, name='pastNews')
]

#url pattern that match the url today and 

