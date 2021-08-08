from django.urls import path
from . views import encrypt , index , decrypt , message 
from django.conf.urls import url

urlpatterns = [
    path('', index , name="Lidark_algorithm"),
    path('encrypt', encrypt , name="encrypt"),
    path('decrypt', decrypt , name="decrypt"),
    path('message', message , name="message"),
    


    


]
