from django.urls import path
from .views import *
from . import views
from .views import HomePageView,AboutUsView,ContactUsView, GameCommentListView, MyCommentsListView

app_name = 'pages'
urlpatterns = [
    path('', PrintGameScore.as_view(), name="math-score-list"),
    path('', GameCommentListView.as_view(), name="comment-list"),
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('my_comment/', MyCommentsListView.as_view(), name='my_comment'),
    path('my_comment/delete/<int:id>', views.delete_math, name='delete'),
    
]

