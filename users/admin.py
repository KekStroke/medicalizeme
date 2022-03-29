from django.contrib import admin

from blog.models import Specialization, Workspace, user_specialization, user_workspace
from .models import Feedback, User, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(Specialization)
admin.site.register(user_specialization)
admin.site.register(Workspace)
admin.site.register(user_workspace)