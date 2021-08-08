from django.urls import path 
from . views import Generate_password 
urlpatterns = [
    
    path('', Generate_password , name='Generate_password'),

    

]
