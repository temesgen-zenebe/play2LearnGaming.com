from django.urls import path
from .views import *
from . import views
from .views import HomePageView,AboutUsView,ContactUsView, GameCommentListView, MyCommentsListView
from pages import views as contact_views
app_name = 'pages'
urlpatterns = [
    path('', PrintGameScore.as_view(), name="math-score-list"),
    path('', GameCommentListView.as_view(), name="comment-list"),
    path('', HomePageView.as_view(), name='homepage'),
     path('subscribe/', views.subscribe, name='subscribe'),
    path('my_comment/', MyCommentsListView.as_view(), name='my_comment'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', contact_views.contact_view, name='contact'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'), 
    path('my_comment/delete/<int:id>', views.deleteCommentMath, name='delete'),
    path('my_comment/delete_anagram/<int:id>', views.deleteCommentAnagrame, name='delete_anagram'),
    path('my_comment/delete_game/<int:id>', views.deleteGameComment, name='delete_game'),
    
]

