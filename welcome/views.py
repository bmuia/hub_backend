from django.http import HttpResponse

def welcome(request):
    """
    A simple view that returns a welcome message.
    """
    return HttpResponse("Welcome to the Hub Backend API!")