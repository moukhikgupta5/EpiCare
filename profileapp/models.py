from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(default= 'User', max_length=200, null=True)

    title = models.CharField(default='Epilypsey Patient', max_length=200, null=True)

    push_bullet_token = models.CharField(default='o.T5jj6vMn2KytwTfbVtmn8o8AzYiHpzfL', max_length=400, null=True)

    profile_img = models.ImageField(default = 'media/default.jpg', upload_to = 'media', null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Seizures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username}'s Seizure at {self.timestamp}"