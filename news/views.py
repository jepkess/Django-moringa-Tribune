from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt


#creating the views here 
def welcome(request):
    return render(request,'welcome.html')
#view function to represent the today news.
def news_of_day(request):
    date=dt.date.today()
    return render(request,'all-news/today-news.html',{'date':date})
#creating a view function that represents the news of the past days.

def past_days_news(request,past_date):
    try:
    # convert data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
          # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request,'all-news/past-news.html',{'date':date})    




  



    