from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.user_index,name='user_index'),
    path('user_profile/',views.user_profile,name='user_profile')
]
