from django.urls import path
from .views import (
    ListJokeView,
    CreateJokeView,
    LikeCreateView,
    VoteCreateView,
    FetchExternalJokeView,
)

urlpatterns = [
    path('jokes/', ListJokeView.as_view(), name='list-jokes'),
    path('jokes/create/', CreateJokeView.as_view(), name='create-joke'),
    path('likes/create/', LikeCreateView.as_view(), name='create-like'),
    path('votes/create/', VoteCreateView.as_view(), name='create-vote'),
    path('jokes/random/', FetchExternalJokeView.as_view(), name='fetch-random-joke'),
]
