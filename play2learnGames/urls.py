from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    #path('anagramGame/', include('anagramGame.urls')),
    #path('mathGame/', include('mathGame.urls')),
    path('', include('anagram_game.urls')),
    path('', include('math_game.urls')),
    path('', include('pages.urls')),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
