from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # this is a model class to add details that the user model doesn't already have.
    # to do that we use one to one mapping
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)  # saves the uploaded image in media/profile_pics folder

    def __str__(self):
        return self.user.username
