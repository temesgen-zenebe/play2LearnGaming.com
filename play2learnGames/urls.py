from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    #path('anagramGame/', include('anagramGame.urls')),
    #path('mathGame/', include('mathGame.urls')),
    path('', include('anagram_game.urls')),
    path('', include('math_game.urls')),
    path('', include('pages.urls')),
]
