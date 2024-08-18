from django.urls import path
from .views import CustomUserListCreateView, LoginView

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    # path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    # path('users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'), #This is used for custom delete 
    path('login/', LoginView.as_view()),
]