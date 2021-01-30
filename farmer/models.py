from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user =  models.CharField(max_length=10, blank=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=350)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    mobile = models.CharField(max_length=10, blank=False,default=False, unique=True)
    email = models.EmailField(max_length=254, blank=False,default=False, unique=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    phone_confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.user




class Image(models.Model):

    image = models.ImageField(upload_to='pictsagram/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50, blank=True)
    imageuploader_profile =  models.CharField(max_length=50, blank=False)
    image_likes = models.ManyToManyField(User, default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null=True)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.imageuploader_profile

    # def number_of_likes(self):
    #     return self.image_likes.count()


class Comment(models.Model):
    post = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

#
# class Comments(models.Model):
#     comment_post = models.CharField(max_length=150)
#     author = models.ForeignKey('Profile', related_name='commenter', on_delete=models.CASCADE)
#     commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.author
