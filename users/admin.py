from django.contrib import admin

# Register your models here.
from .models import Profile, Child, Message

admin.site.register(Profile)
admin.site.register(Child)
admin.site.register(Message)