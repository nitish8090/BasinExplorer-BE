from django.urls import path, include

urlpatterns = [
    path('User/', include('UserApp.urls')),
    path('BasinManager/', include('BasinManager.urls'))
]
