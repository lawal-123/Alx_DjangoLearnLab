# accounts/serializers.py
from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user
from rest_framework import serializers
from .models import CustomUser

# Serializer for User Registration
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # We only need to expose these fields during registration
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # Override the create method to correctly hash the password
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class CustomUserProfileSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'id', 
            'username', 
            'email', 
            'bio', 
            'profile_picture', 
            'follower_count', 
            'following_count'
        )
        read_only_fields = ('username', 'email', 'follower_count', 'following_count') # Username/email are typically not changeable

    def get_follower_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
