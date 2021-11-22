from django.http import HttpResponse

#creating views here 
def welcome(request): # welcome is our view function.
    return HttpResponse('Welcome to the moringa Tribune')
