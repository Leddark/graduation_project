from django.urls import path 
from . views import sub_domains 
urlpatterns = [
    
    path('', sub_domains , name='sub_domin'),

    

]
