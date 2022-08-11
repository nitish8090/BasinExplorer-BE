from rest_framework.authtoken import views
from django.urls import path


urlpatterns = [
    path('GetToken/', views.obtain_auth_token)
]