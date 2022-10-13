from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
