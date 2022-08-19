from django.urls import path
from .views import *
from .views import HomePageView,AboutUsView,ContactUsView, GameCommentListView

app_name = 'pages'
urlpatterns = [
    path('', PrintGameScore.as_view(), name="math-score-list"),
    path('', GameCommentListView.as_view(), name="comment-list"),
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]

