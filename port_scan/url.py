from django.urls import path 
from . views import port_scan 
urlpatterns = [
    
    path('', port_scan , name='port_scan'),
    

    

]
