from django.urls import path
from .views.custom_user import*
from .views.otp import OtpViewSet
urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('users/delete/<int:pk>', CustomUserDeleteView.as_view(), name='user-delete'), #This is used for custom delete 
    path('login/', LoginView.as_view()),
    path('users/send_otp', OtpViewSet.as_view({'post': 'create_otp'}), name='user-send-otp'), #This is used for send Otp for the User mail 
    path('users/verify_otp', OtpViewSet.as_view({'post': 'verify_otp'}), name='user-verify-otp'),#This is used for verify Otp for the User 
]