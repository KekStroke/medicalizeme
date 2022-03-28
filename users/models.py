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

    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    first_login = models.DateTimeField(null=True)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default=PATIENT)
    # blank for forms, null for database
    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)

    objects = UserManager()

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES=[
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
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