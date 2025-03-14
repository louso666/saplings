from django.contrib import admin
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid', 'last_login')
    search_fields = ('user__username', 'uid', 'provider')
    list_filter = ('provider',)

@admin.register(SocialApp)
class SocialAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'client_id')
    search_fields = ('name', 'provider', 'client_id')

@admin.register(SocialToken)
class SocialTokenAdmin(admin.ModelAdmin):
    list_display = ('app', 'account', 'token')
    search_fields = ('app__name', 'account__uid')
