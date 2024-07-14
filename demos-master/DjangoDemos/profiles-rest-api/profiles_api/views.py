import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from profiles_api import permissions, serializers
from rest_framework import filters

from rest_framework import viewsets

from profiles_api import models
from profiles_api.models import Book, Post  # Import the status module

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.


class BookApiView(APIView):

    serializer_class = serializers.BookSerializer

    def get(self, request):
        """Returns a list of APIView features"""

        books = Book.objects.all().values()
        return Response({'books': list(books)})

    def post(self, request):
        """post method to add new Book"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            author = serializer.validated_data.get('author')
            book = Book.objects.create(title=title, author=author)
            # Book.save(book)
            message = f'Book Added {book}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.BookModelSerializer

    queryset = Book.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.PostModelSerializer

    queryset = Post.objects.all()


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
        # IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserProfileApiView(APIView):

    def get(self, request):
        """Returns a list of APIView features"""

        users = models.UserProfile.objects.all().values()
        return Response({'users': list(users)})

    serializer_class = serializers.UserProfileSerializer

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            user = models.UserProfile.objects.create(name=name, email=email)
            models.UserProfile.save(user)
            message = f'User Added {user}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request):
        """Returns a list of APIView features"""

        return Response({'message': 'Hello!'})

    serializer_class = serializers.HelloSerializer

    def post(self, request):
        """Create a hello message with our name"""

        # name = request.data.get('name')
        # return Response({'message': f'Hello {name}'})

        # # without using serializer - no validation for data

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # def put(self, request, pk=None):
    #     """Handle updating an object"""

    #     return Response({'method': 'PUT'})

    # def patch(self, request, pk=None):
    #     """Handle partial update of object"""

    #     return Response({'method': 'PATCH'})

    # def delete(self, request, pk=None):
    #     """Delete an object"""

    #     return Response({'method': 'DELETE'})


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# add LaptopViewSet class
