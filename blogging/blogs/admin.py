from django.contrib import admin
from .models import BlogPost,Comment,UserProfile,CommentReaction
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(CommentReaction)
