from django.contrib import admin
from social_django.models import UserSocialAuth, Association, Nonce

admin.site.register(UserSocialAuth)
admin.site.register(Association)
admin.site.register(Nonce)

# Register your models here.
