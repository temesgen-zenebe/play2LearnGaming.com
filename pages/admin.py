from django.contrib import admin
from .models import Games_comment, SubscribedUsers,SiteVisitersCounter,Contact
 
# Register your models here.
@admin.register(Games_comment)
class GamesComment(admin.ModelAdmin):
    list_display = ('user', 'email', 'comment', 'created','active',)
    list_filter = ('active', 'created')
    search_fields = ('user', 'email' 'created')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
        

@admin.register(SubscribedUsers )
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')
    
@admin.register(SiteVisitersCounter)
class SiteVisitersCounterAdmin(admin.ModelAdmin):
    list_display = ('visits_num', 'updated_date')
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ('full_name','email','subject','message','created_date')
     

     

     
     