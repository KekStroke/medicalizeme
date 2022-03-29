from django.contrib import admin
from .models import Feedback, User, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Feedback)