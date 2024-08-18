# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.views import APIView
# from .models.custom_user import CustomUser
# from django.shortcuts import get_object_or_404
# from .serializers import CustomUserSerializer, LoginSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.hashers import check_password
# import pdb

# from rest_framework import status
# from rest_framework.response import Response

# # This is used for create and index
# class CustomUserListCreateView(generics.ListCreateAPIView):
#   queryset = CustomUser.objects.all()
#   serializer_class = CustomUserSerializer

#   def list(self, request, *args, **kwargs):
#     # pdb.set_trace() #This can be used as byebug
#     response = super().list(request, *args, **kwargs)
#     # Add additional data to the response
#     response_data = {
#         'message': 'User list fetched successfully',
#         'total_users': len(response.data),
#         'users': response.data
#     }
#     # response.data['total_users'] = len(response.data['results'])
#     return Response(response_data)    
    
# # This can be used for update, show, delete
# # class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
# #   queryset = User.objects.all()
# #   serializer_class = UserSerializer

# # # This can be used for custom purpose
# # class UserDeleteView(APIView):
# #   def delete(self, request, *args, **kwargs):

# #     # pdb.set_trace() #This can be used as byebug
# #     user_id = kwargs.get('pk')
# #     user = get_object_or_404(User, pk=user_id)
# #     user.delete()
# #     return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class LoginView(APIView):
#   def post(self, request):
#     try:
#       data = request.data
#       serializer = LoginSerializer(data=data)
#       if serializer.is_valid():
#         email = serializer.data.get('email')
#         user = CustomUser.objects.get(email=email, password=password)
#         password = check_password(serializer.data.get('password'), user.password)
#         if user is None:
#           return Response({"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
#         refresh = RefreshToken.for_user(user)

#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#       return Response({"message": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# # This can be used for Otp send to User purpose
# class OtpViewSet(ModelViewSet):
#   serializer_class = OtpSerializer
#   queryset = Otp.objects.all()

#   # @action(detail=False, methods=['post'], url_path='create-otp')
#   def create_otp(self, request):
#     otp = pyotp.TOTP('base32secret3232').now()
#     recipient_email = request.data.get('email')

#     if recipient_email:
#       otp_instance, created = Otp.objects.update_or_create(
#         email=recipient_email,
#         defaults={'code': otp}
#       )

#       subject = 'OTP Created'
#       message = f'Your OTP: {otp}'
#       from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set in your settings

#       try:
#         send_mail(subject, message, from_email, [recipient_email])
#         return Response({'message': 'OTP created and email sent'}, status=status.HTTP_201_CREATED)
#       except Exception as e:
#         return Response({'error': f'Error sending email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

#   # @action(detail=False, methods=['post'], url_path='verify-otp')
#   def verify_otp(self, request):
#     serializer = OtpSerializer(data=request.data)
#     pdb.set_trace()
#     if serializer.is_valid():
#       email = serializer.validated_data['email']
#       code = serializer.validated_data['code']
#       try:
#         otp_instance = Otp.objects.get(email=email)
#         if otp_instance.code == code:
#           return Response({'message': 'OTP is valid'}, status=status.HTTP_200_OK)
#         else:
#           return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
#       except Otp.DoesNotExist:
#           return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


