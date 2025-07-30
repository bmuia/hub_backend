from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserSerializer 
from django.shortcuts import get_object_or_404
from django.utils import timezone
import logging
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


logger = logging.getLogger(__name__)

# Custom JWT token serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['anonymous_unique_id'] = user.anonymous_unique_id

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# get all users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# get single user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# sign up new user (only admin user can regiser a new user)
@api_view(['POST'])
@permission_classes([AllowAny])  
def registerUser(request):
    if not request.user.is_staff:
        return Response(
            {"message": "You do not have permission to perform this action."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Generate JWT token after successful registration
        refresh = CustomTokenObtainPairSerializer.get_token(user)
        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    else:
        logger.error(f"Registration errors: {serializer.errors}")
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

# sign in user
@api_view(['POST'])
@permission_classes([AllowAny])
def loginUser(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(email=serializer.validated_data['email'])
        refresh = CustomTokenObtainPairSerializer.get_token(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    else:
        logger.error(f"Login errors: {serializer.errors}")
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

# delete user
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response(
        {"message": "User account successfully deleted!"},
        status=status.HTTP_204_NO_CONTENT
    )

