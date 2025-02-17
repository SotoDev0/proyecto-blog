from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categorias.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255,unique=True)
    miniature = models.ImageField(upload_to='post/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete=SET_NULL,null=True)

    # representa el objeto en un formato legible para los humanos, como una cadena de texto.
    def __str__(self):
        return self.title
    
    



