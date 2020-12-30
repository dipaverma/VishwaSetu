from django.db import models

class User(models.Model):
    username = models.OneToOneField("username", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    bio = models.CharField(max_length = 200)
    profile_pic = models.ImageField(upload_to = 'ProfilePicture/')
    date = models.DateTimeField(auto_add_now = True, null=True)
    follow = models.ManyToMany("self")

    def __str__(self):
        return self.username

class Post(models.Model):
    image = models.ImageField(upload_to="posts/")
    image_caption = models.CharField(max_length = 200)
    uploader = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.IntegerField()
    