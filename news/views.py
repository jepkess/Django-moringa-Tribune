from django.http import HttpResponse,Http404
import datetime as dt

# creating views here


def welcome(request):  # welcome is our view function.
    return HttpResponse('Welcome to the moringa Tribune')

# adding the dynamic content to our application.

# view function that is responsible for returning news of the specific day.


def news_of_day(request):
    # calling the date.today function to get the current date.
    date = dt.date.today()

    # function that convert the date object to find specific day.
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
               <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    </html>    
    
    '''
    return HttpResponse(html)
# function that get the weekday number by the date.


def convert_dates(dates):
    # function that takes in date and return a number that represent specific day of the week.
    day_number = dt.date.weekday(dates)

    days = ['monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Returning the actual day of the week.
    day = days[day_number]
    return day
# function that get the past news date


def past_days_news(request, past_date):
    try:
    # convert data from the string url
     date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
          # Raise 404 error when ValueError is thrown
        raise Http404()

    day = convert_dates(date)
    html = f'''
    <html>
        <body>
            <h1> News for {day} {date.day}-{date.month}-{date.year} </h1>
        </body>+
    </html>
    '''
    return HttpResponse(html)

from django.shortcuts import render

#creating the views here 
def welcome(request):
    return render(request,'welcome.html')
