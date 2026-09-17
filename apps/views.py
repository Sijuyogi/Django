from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'Name':'SijuYogi'
    },
    {
        'Name' :'VinithXavier'
    }
]

def home(request):
    return render(request,'apps/home.html')
def about(request):
    return render(request,'apps/about.html')
def contact(request):
    return render(request,'apps/contacts.html')
def post(request):
    context={
        'posts':posts
    }
    return render(request,'apps/posts.html',context=context)