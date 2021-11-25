from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 
from django.urls import path



#list of urls instance for our application.
urlpatterns=[
   
    path('',views.news_today, name='newsToday'), #urlpattern for the new_of_ day view function.
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news, name='pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    #defining a urlpattern for a single article.
    url(r'^article/(\d+)',views.article,name ='article')
]
#configuring the urls path to register for the MEDIA-ROOT
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




