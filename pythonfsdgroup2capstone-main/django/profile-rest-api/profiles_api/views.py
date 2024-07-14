from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import permissions, serializers
from profiles_api import models
from profiles_api.models import Book, Employee
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Movie, Movierelease,Tickets
from .serializers import MovieSerializer, MoviereleaseSerializer, Ticketsializer


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request):
        """Returns a list of APIView features"""

        return Response({'message': 'Hello!'})
    serializer_class = serializers.HelloSerializer

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        # name = request.data.get('name')
        # return Response({'message': f'Hello {name}'})
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.BookModelSerializer

    queryset = Book.objects.all()

class EmpViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.EmpModelSerializer

    queryset = Employee.objects.all()
    
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
            
class EmpApiView(APIView):

    serializer_class = serializers.EmpModelSerializer

    def get(self, request):
        """Returns a list of APIView features"""

        Employees = Employee.objects.all().values()
        return Response({'Employee': list(Employees)})
    
    def post(self, request):
        """post method to add new Book"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            name = serializer.validated_data.get('name')
            salary = serializer.validated_data.get('salary')
            project = serializer.validated_data.get('project')
            emp = Employee.objects.create(id=id, name=name,salary=salary,project=project )
            # Book.save(book)
            message = f'Employee Added {emp}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )
        # IsAuthenticated - #for only logged in can read the data

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Ticketsializer
    queryset = Tickets.objects.all()

class MoviereleaseViewSet(viewsets.ModelViewSet):
    queryset = Movierelease.objects.all()
    serializer_class = MoviereleaseSerializer    
