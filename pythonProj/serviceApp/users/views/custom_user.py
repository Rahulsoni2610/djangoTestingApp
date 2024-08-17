from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from ..models.custom_user import CustomUser
from django.shortcuts import get_object_or_404
from ..serializers import CustomUserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
import pdb

from rest_framework import status
from rest_framework.response import Response

# This is used for create and index
class CustomUserListCreateView(generics.ListCreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      response_data = {
          'user': serializer.data,
          'message': "User's account created successfully"
      }
      return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

  def list(self, request, *args, **kwargs):
    response = super().list(request, *args, **kwargs)
    # Add additional data to the response
    response_data = {
        'message': "Users list fetched successfully",
        'total_users': len(response.data),
        'users': response.data
    }
    # response.data['total_users'] = len(response.data['results'])
    return Response(response_data)    
    
# This can be used for update, show, delete
class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

  def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User's account deleted successfully"}, status=status.HTTP_200_OK)

  def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # Create a custom response with a success message and updated data
        response_data = {
            'user': serializer.data,
            'message': "User's account updated successfully"
        }
        return Response(response_data, status=status.HTTP_200_OK)

# # This can be used for custom purpose
class CustomUserDeleteView(APIView):
  def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        user.delete()
        return Response({"message": "User's account deleted successfully"}, status=status.HTTP_200_OK)


class LoginView(APIView):
  def post(self, request):
    try:
      data = request.data
      serializer = LoginSerializer(data=data)
      if serializer.is_valid():
        email = serializer.data.get('email')
        user = CustomUser.objects.get(email=email, password=password)
        password = check_password(serializer.data.get('password'), user.password)
        if user is None:
          return Response({"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({"message": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)