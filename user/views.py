from django.shortcuts import render

# Create your views here.

def user_index(request):
    return render(request,'user/user_index.html')

def user_profile(request):
    return render(request,'user/user_profile.html')