# accounts/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import CustomUserRegistrationSerializer, CustomUserProfileSerializer
from .models import CustomUser

# View for User Registration
class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
    # Allow any user (unauthenticated) to register
    permission_classes = [permissions.AllowAny]

# Custom View for Login (ObtainAuthToken) to return more data
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # The token is created automatically upon user creation if 'rest_framework.authtoken' is installed
        token, created = Token.objects.get_or_create(user=user)
        
        # Return the token and user details upon successful login
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# View for User Profile (Retrieve/Update)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserProfileSerializer
    # Only authenticated users can access their profile
    permission_classes = [permissions.IsAuthenticated]

    # The lookup field should be the primary key (pk) of the user
    def get_object(self):
        return self.request.user # Ensure the user can only see/edit their own profile