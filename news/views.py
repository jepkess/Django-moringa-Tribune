from django.http import HttpResponse

#creating views here 
def welcome(request):
    return HttpResponse('Welcome to the moringa Tribune')
