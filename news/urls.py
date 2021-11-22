from django.conf.urls import url
from . import views 


#list of urls instance for our application.
urlpatterns=[
    url('^$',views.welcome, name='welcome'),
]

