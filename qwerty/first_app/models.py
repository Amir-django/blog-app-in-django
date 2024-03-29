from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"publish")
)

class post(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(max_length=200)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS ,default=0)

class meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title
