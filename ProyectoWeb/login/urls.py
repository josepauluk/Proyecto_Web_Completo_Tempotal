from django.urls import path

from .views import  VistaLogin, cerrar_sesion


urlpatterns = [    
        
    path('', VistaLogin.as_view(), name='Login'),    

    path('', cerrar_sesion, name='cerrar_sesion'),
]


