
from django.contrib import admin
from django.urls import path, include 




urlpatterns = [
    path('admin/', admin.site.urls),
    #Se agrego la ruta para el login de usuario
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accpunts.urls')), # new
    path('', include('appblog.urls')),

]
