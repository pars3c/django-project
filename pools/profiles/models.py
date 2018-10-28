from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    '''
    OneToOneField(User) will extend the class User and all it's fields, while also letting us add new fields
    that the User class does not have
    '''
    user = models.OneToOneField(User)

    '''
    additional fields will be portfolio_site and profile picture
    '''
    
    
    # blank=True means that field is not mandatory
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
        