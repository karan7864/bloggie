# appname/models.py

from django.db import models
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    info_bar = models.CharField(max_length=300, null=True, unique=False)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100,null=True,unique=False)
    blog_category = models.CharField(max_length=100,null=True,unique=False)
    blogger = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blogger',null=True,unique=False)


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, null=True, unique=False)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog_post}'


class CommentReaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='reactions', null=True)
    reaction = models.BooleanField( null=True)

    class Meta:
        unique_together = ('user', 'comment')


class UserProfile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, null=True, unique=False)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)



