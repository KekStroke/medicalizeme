from django.contrib import admin

from .models import Feedback, Follower, User, Profile, Specialization, Workspace, user_specialization, user_workspace

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(Feedback)
admin.site.register(Specialization)
admin.site.register(user_specialization)
admin.site.register(Workspace)
admin.site.register(user_workspace)