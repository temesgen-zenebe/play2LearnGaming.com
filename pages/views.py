
from django.views.generic import TemplateView,ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from anagram_game.models import Anagram_score,Comment_Anagram
from math_game.models import Addition_score,Division_score,Multiplication_score,Subtraction_score,Comment_math
from anagram_game.forms import CommentAnagrameForm
from math_game.forms import CommentForm 
from users.models import LoggedUser 
from django.contrib.auth import get_user_model
from django.db.models import F
from .models import Games_comment 
from .forms import GameCommentForm
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.core.validators import validate_email
from .models import SubscribedUsers,SiteVisitersCounter,Contact
from .forms import ContactForm
from common.utils.email import send_email
from django.conf import settings

#get time date 
today = timezone.now()
startDate = today - timedelta(days=7)
endDate = today 


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender = 'temf2006@gmail.com'# system email
            subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            to = 'egolebearingplc@gmail.com'# admin email
            content = form.cleaned_data['message']
            send_email(to, subject, content, sender)
            return render(request, 'pages/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/contact_us.html', context)

def owners_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender = 'temf2006@gmail.com'# system email
            subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            to = 'egolebearingplc@gmail.com'# admin email
            content = form.cleaned_data['message']
            send_email(to, subject, content, sender)
            return render(request, 'pages/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/about_us.html', context)


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
     
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'
    
class MyCommentsListView(View):
    
    def get(self, request):
         ana_comment = Comment_Anagram.objects.filter(Q(user = request.user) ).order_by('-created').distinct('created')
         math_comment = Comment_math.objects.filter(Q(user = request.user) ).order_by('-created').distinct('created')
         
         #comment
         game_comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
         context = {
             'my_anagram_comment' : ana_comment,
             'my_math_comment': math_comment,  
             'game_comment':game_comment,
             
         }
         return render(request, 'pages/my_comment.html', context)
     
    def post(self, request):
        if request.POST.get('game_type') == 'anagrame':# anagrame game
                data = {  
                        'game_type' : request.POST.get('game_type'),
                        'comment' : request.POST.get('comment'), 
                        }
                forms = CommentAnagrameForm(data)
                if forms.is_valid():
                    commentNew = Comment_Anagram.objects.create(
                    user = request.user,
                    game_type = request.POST.get('game_type'),
                    comment = request.POST.get('comment'),
                    )
                    commentNew.save()
                    messages.success(request, 'your comment submited successfully !!.')
                    return redirect('pages:my_comment')
                else:
                    return render(request,"pages/my_comment.html",{})
         
        else :# math game
            
            data = {  
                'game_type' : request.POST.get('game_type'),
                'comment' : request.POST.get('comment'), 
            }
            forms = CommentForm(data)
            if forms.is_valid():
                commentNew = Comment_math.objects.create(
                    user = request.user,
                    game_type = request.POST.get('game_type'),
                    comment = request.POST.get('comment'), 
                )
                commentNew.save()
                return redirect('pages:my_comment')
            else:   
                return render(request,"pages/my_comment.html",{})
                          
class GameCommentListView(ListView):
   template_name = 'pages/home.html'
   model = Games_comment
   context_object_name = 'games_comment'

   def get_queryset(self):
       comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
       return comment
    


class PrintGameScore(View):
     
    def get(self, request):
        
        #about math game
        operate1 = Addition_score.objects.all().order_by('-point').distinct('point')
        operate2 = Division_score.objects.all().order_by('-point').distinct('point')
        operate3=  Multiplication_score.objects.all().order_by('-point').distinct('point')
        operate4 = Subtraction_score.objects.all().order_by('-point').distinct('point')
        # about 
        anagramScore = Anagram_score.objects.all().order_by('-point').distinct('point')
        
        #comment
        comment = Games_comment.objects.filter(Q(active = True)).order_by('-created').distinct('created')
        
        #user information 
        logged_users=LoggedUser.objects.all()
        numbers_users = get_user_model().objects.all().count()
        weekly_signup = get_user_model().objects.filter(date_joined__range=[startDate,endDate]).count()
        #SubscribedUsers
        
        Subscribed_users = SubscribedUsers.objects.all().count()
        #print(weekly_signup)
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        numVisits = request.session['num_visits']
        num = numVisits
        totalNumVisits = num + numVisits
        context = {
            'Addition':operate1,
            'Division':operate2,
            'Multiplication':operate3,
            'Subtraction':operate4,
            'anagramScore':anagramScore,
            'gameComment':comment,
            'logged_users': logged_users,
            'numbers_users': numbers_users,
            'weekly_signup':weekly_signup,
            'num_visits': totalNumVisits,
            'Subscribed_users':Subscribed_users
        
        }
        return render(request, 'pages/home.html', context)
    
    def post(self, request):
        data = {  'email' : request.POST.get('email'),
                  'comment' : request.POST.get('comment'),
                }
        forms = GameCommentForm(data)
        if forms.is_valid():
            commentNew = Games_comment.objects.create(
                  user = request.user,
                  email = request.POST.get('email'),
                  comment = request.POST.get('comment'), 
              )
            commentNew.save()
            return redirect('pages:math-score-list')
        else:   
            return render(request,"pages/home.html",{})

def deleteCommentMath(request, id):
  member = Comment_math.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('pages:my_comment'))
    
def deleteCommentAnagrame(request, id):
  member = Comment_Anagram.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('pages:my_comment'))

def deleteGameComment(request, id):
  member = Games_comment.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('pages:my_comment'))

        
def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))  
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
        
       
