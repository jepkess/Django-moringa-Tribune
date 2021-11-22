from django.conf.urls import url
from . import views 

#list of urls instance for our application.
urlPatterns=[
    url('^&',views.welcome, name='welcome'),
]