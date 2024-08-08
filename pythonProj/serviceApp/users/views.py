from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
import pdb

from rest_framework import status
from rest_framework.response import Response

# This is used for create and index
class UserListCreateView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request, *args, **kwargs):
    # pdb.set_trace() #This can be used as byebug
    response = super().list(request, *args, **kwargs)
    # Add additional data to the response
    response_data = {
        'message': 'User list fetched successfully',
        'total_users': len(response.data),
        'users': response.data
    }
    response.data['total_users'] = len(response.data['results'])
    return Response(response_data)    
    
# This can be used for update, show, delete
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# This can be used for custom purpose
class UserDeleteView(APIView):
  def delete(self, request, *args, **kwargs):

    # pdb.set_trace() #This can be used as byebug
    user_id = kwargs.get('pk')
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)