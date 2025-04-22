from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.user_enquiry_index,name='user_enquiry_index'),
    path('user_enquiry_registor_form/',views.user_enquiry_index_registor_form,name='user_enquiry_registor_form')
]
