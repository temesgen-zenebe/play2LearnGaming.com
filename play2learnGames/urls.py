from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('anagramGame/', include('anagramGame.urls')),
    #path('mathGame/', include('mathGame.urls')),
    path('', include('anagramGame.urls')),
    path('', include('mathGame.urls')),
    path('', include('pages.urls')),
]
