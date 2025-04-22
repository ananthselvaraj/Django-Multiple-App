from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.user_list_index,name='user_list_index'),
    path('user_list_details/',views.user_list_details,name='user_list_details')
]
