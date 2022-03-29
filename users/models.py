from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse

from uuid import UUID, uuid4
from PIL import Image

class User(AbstractUser):
    DOCTOR = 'DOC'
    PATIENT = 'PAT'
    USER_TYPE_CHOICES=[
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    ]

    # id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    first_login = models.DateTimeField(null=True)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default=PATIENT)
    # blank for forms, null for database
    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)

    objects = UserManager()


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES=[
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    # id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    years_experience = models.PositiveSmallIntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False, null=False)
    verification_certificate = models.FileField(upload_to='user/certificates/', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})


class Feedback(models.Model):
    # id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    parent = models.OneToOneField('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='feed_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")
        ordering=('date_posted',)
    
    def __str__(self):
        return f'Comment {self.id} by {self.author.username}'


class Specialization(models.Model):
    name = models.CharField(max_length=255)


class user_specialization(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    years_of_experience = models.PositiveSmallIntegerField(null=True, blank=True)


class Workspace(models.Model):
    name = models.CharField(max_length=500)


class user_workspace(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    years_working = models.PositiveSmallIntegerField(null=True, blank=True)
