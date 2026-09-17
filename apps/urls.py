from django.urls import path
from  apps.views import home,about,contact,post 

urlpatterns = [
    path('', home , name='app-home'),
    path('about/', about , name='about-app'),
    path('contact/',contact , name='contact-app'),
    path('post/', post, name='app-post')
]