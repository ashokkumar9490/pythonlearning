from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from profiles_project import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    

class Book(models.Model):
    """Database model for books"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of book"""
        return self.title + ' by ' + self.author


class Employee(models.Model):
    """Database model for books"""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.CharField(max_length=10)
    project = models.CharField(max_length=100)  

    def __str__(self):
        """Return string representation of book"""
        return self.id + ' , ' + self.name + ' , ' + self.Salary +' , ' + self.Projects
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text



class Movie(models.Model):
    """Database model for books"""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    desc = models.TextField()
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    director = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name


class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    theatre =models.CharField(max_length=255)
    total =  models.IntegerField(max_length=10)
    noSeats = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Movierelease(models.Model):
    """Database model for books"""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    

    def __str__(self):
        return self.name