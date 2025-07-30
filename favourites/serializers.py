from rest_framework import serializers
from .models import Joke, Like, Vote


class JokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Joke
        fields = ['id','category','content','created_at']
        read_only_fields  = ['id','created_at']

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id','user','joke','is_liked','created_at']
        read_only_fields = ['id','user','is_liked','created_at']


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id','user','joke','vote_type','created_at']
        read_only_fields = ['id','created_at','user']