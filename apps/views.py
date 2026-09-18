from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'Name':'SijuYogi',
        'Age':27
    },
    {
        'Name' :'VinithXavier',
        'Age':28
    }
]

def home(request):
    return render(request,'apps/home.html', {'title':'App-Home'})
def about(request):
    return render(request,'apps/about.html')
def contact(request):
    return render(request,'apps/contacts.html')
def post(request):
    context={
        'posts':posts
    }
    return render(request,'apps/posts.html',context=context)