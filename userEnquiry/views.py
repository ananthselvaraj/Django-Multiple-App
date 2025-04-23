from django.shortcuts import render

# Create your views here.

def user_enquiry_index(request):
    return render(request,'userenquiry/user_enquiry_index.html')

def user_enquiry_index_registor_form(request):
    return render(request,'userenquiry/user_enquiry_registor_form.html')