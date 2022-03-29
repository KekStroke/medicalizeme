from django.db import models
from django.forms import CharField
from django.urls import reverse

from users.models import User

class Appointment(models.Model):

    FREE = 'FR'
    CHECK_IN = 'CH'
    SET = 'ST'
    STATUS_CHOICES = [
        (FREE, 'free'),
        (CHECK_IN, 'checked in'),
        (SET, 'set'),
    ]

    date = models.DateField()
    timeslot = CharField(max_length=5)
    date_requested = models.DateTimeField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doc_appointment')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pat_appointment')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=FREE)

    class Meta:
        verbose_name = ("Appointment")
        verbose_name_plural = ("Appointments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Appointment_detail", kwargs={"pk": self.pk})