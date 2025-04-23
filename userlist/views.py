from django.shortcuts import render

# Create your views here.

def user_list_index(request):
    return render(request,'userlist/user_list_index.html')

def user_list_details(request):
    return render(request,'userlist/user_list_details.html')
