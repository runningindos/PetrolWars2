from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Station(models.Model):
    station = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.station