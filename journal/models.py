from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"Entry for {self.user.username} on {self.date}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

