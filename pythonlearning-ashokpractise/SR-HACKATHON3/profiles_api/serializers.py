from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class BookSerializer(serializers.Serializer):
    """Serializes title and author fields for BookAPIView"""
    title = serializers.CharField(max_length=20)
    author = serializers.CharField(max_length=20)


class BookModelSerializer(serializers.ModelSerializer):
    """Serializes title and author fields for BookAPIView"""
    class Meta:
        model = models.Book
        fields = ('title', 'author')


class PostModelSerializer(serializers.ModelSerializer):
    """Serializes Post model"""
    class Meta:
        model = models.Post
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


# id = models.models.IntegerField
#     modelname = models.CharField(max_length=20)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     ram   = models.CharField(max_length=10)
#     description = models.CharField(max_length=20)

# add serializer for Laptop
class LaptopModelSerializer(serializers.ModelSerializer):

    """Serializes title and author fields for BookAPIView"""

    class Meta:

        model = models.Laptop 

        fields = ('id', 'modelname', 'price', 'ram', 'description')

