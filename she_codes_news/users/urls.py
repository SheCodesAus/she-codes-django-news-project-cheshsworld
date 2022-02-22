from django.urls import path
from .views import CreateAccountView
from . import views


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', views.UserProfile.as_view(), name='profile'),  
    path('<int:pk>/update', views.UpdateUserView.as_view(), name='updateProfile')  
    ]