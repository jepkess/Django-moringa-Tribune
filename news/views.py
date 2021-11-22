from django.http import HttpResponse
import datetime as dt

# creating views here


def welcome(request):  # welcome is our view function.
    return HttpResponse('Welcome to the moringa Tribune')

# adding the dynamic content to our application.

#view function that is responsible for returning news of the specific day.
def news_of_day(request): 
    date = dt.date.today() # calling the date.today function to get the current date.

    #function that convert the date object to find specific day.
    day= convert_dates(date)
    html = f'''
        <html>
            <body>
               <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    </html>    
    
    '''
    return HttpResponse(html)
#function that get the weekday number by the date.
def convert_dates(dates):
    day_number=dt.date.weekday(dates) # function that takes in date and return a number that represent specific day of the week.

    days=['monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    #Returning the actual day of the week.
    day=days[day_number]
    return day


