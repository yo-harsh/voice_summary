"""URL mappings for the user API.
"""
from django.urls import path

from user import views as user_views


app_name = 'user'

urlpatterns = [
    path('create/', user_views.CreateUserView.as_view(), name='create')
]
