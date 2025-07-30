from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Joke(models.Model):
    content = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])
    created_at = models.DateTimeField(auto_now_add=True)
