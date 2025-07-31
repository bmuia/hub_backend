from django.shortcuts import render, redirect
from .models import Joke

# Create a new Todo
def create_joke(request):
    if request.method == 'POST':
        joke = request.POST['joke']
        Joke.objects.create(joke=joke)
        return redirect('list_jokes')
    return render(request, 'hub_backend/create_jokes.html')

def list_jokes(request):
    jokes = Joke.objects.all()
    return render(request, 'hub_backend/list_jokes.html', {'jokes': jokes})    