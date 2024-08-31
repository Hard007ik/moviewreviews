from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emails(models.Model):
    emailid = models.EmailField(max_length=200,unique=True)

    def __str__(self):
        return self.emailid
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='movie/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    text = models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text