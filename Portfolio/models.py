from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=300)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('Project_Detail',kwargs={'pk':self.pk})

    def __str__(self):
        self.project_name

class Comment(models.Model):
    post = models.ForeignKey('Portfolio.Project',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('Resume')

    def __str__(self):
        return self.text


