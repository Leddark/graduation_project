from django.urls import path 
from . views import Home , Assess , massage ,path_security ,CV_Ahmed , Login , Sign_Up , Sign_Up_Send
urlpatterns = [
    
    path('Home', Home , name='Home'),
    path('Assess', Assess , name='Assess'),
    path('massage', massage , name='massage'),
    
    path('path_security', path_security , name='path_security'),
    path('CV_Ahmed', CV_Ahmed , name='CV_Ahmed'),

    path('', Login , name='login'),

    path('Sign_Up', Sign_Up , name='Sign_Up'),
    path('Sign_Up_Send', Sign_Up_Send , name='Sign_Up_Send')

    

]
