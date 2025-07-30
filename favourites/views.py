from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Joke, Like, Vote
from .serializers import JokeSerializer, LikeSerializer, VoteSerializer
import requests

class ListJokeView(generics.ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class CreateJokeView(APIView):
    def post(self, request):
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeCreateView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            joke_id = serializer.validated_data['joke'].id
            if Like.objects.filter(user=request.user, joke_id=joke_id).exists():
                return Response({'error': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(user=request.user, is_liked=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteCreateView(APIView):
    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FetchExternalJokeView(APIView):
    def get(self, request):
        res = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode&type=single")
        if res.status_code == 200:
            data = res.json()
            joke = Joke.objects.create(
                content=data.get('joke'),
                category=data.get('category', 'General')
            )
            
            return Response({
                'id': joke.id,
                'content': joke.content,
                'category': joke.category,
                'created_at': joke.created_at
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Failed to fetch joke'}, status=500)
