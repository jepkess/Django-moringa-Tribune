from django.http import HttpResponse
import datetime as dt

# creating views here


def welcome(request):  # welcome is our view function.
    return HttpResponse('Welcome to the moringa Tribune')

# adding the dynamic content to our application.

#view function that is responsible for returning news of the specific day.
def news_of_day(request): 
    date = dt.date.today() # calling the date.today function to get the current date.
    html = f'''
        <html>
            <body>
               <h1>{date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    </html>    
    
    '''
    return HttpResponse(html)
