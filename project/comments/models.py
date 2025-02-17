from django.db import models
from users.models import User
from django.db.models import CASCADE
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE,null=False)
    post = models.ForeignKey(Post,on_delete=CASCADE,null=False)


    def __str__(self):
        return self.content