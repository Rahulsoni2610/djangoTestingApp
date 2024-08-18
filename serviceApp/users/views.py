from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models.custom_user import CustomUser
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
import pdb

from rest_framework import status
from rest_framework.response import Response

# This is used for create and index
class CustomUserListCreateView(generics.ListCreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

  def list(self, request, *args, **kwargs):
    # pdb.set_trace() #This can be used as byebug
    response = super().list(request, *args, **kwargs)
    # Add additional data to the response
    response_data = {
        'message': 'User list fetched successfully',
        'total_users': len(response.data),
        'users': response.data
    }
    # response.data['total_users'] = len(response.data['results'])
    return Response(response_data)    
    
# This can be used for update, show, delete
# class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# # This can be used for custom purpose
# class UserDeleteView(APIView):
#   def delete(self, request, *args, **kwargs):

#     # pdb.set_trace() #This can be used as byebug
#     user_id = kwargs.get('pk')
#     user = get_object_or_404(User, pk=user_id)
#     user.delete()
#     return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            user = CustomUser.objects.filter(email=email).first()
            
            if user and check_password(password, user.password):

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)