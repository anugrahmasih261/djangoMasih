from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #here oneToone helps to create only 1 profile per user
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

# above in user when we type on_delete=models.CASCADE it means when a user is deleted his profile will also get deleted
# above in created auto_now= True means get the exact date time
