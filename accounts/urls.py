from django.urls import path
from accounts.views import login_page, register_page, activation

urlpatterns = [
    path('login',login_page,name='login'),
    path('register',register_page,name='register'),
    path('activate/<email_token>',activation,name='activate'),
]