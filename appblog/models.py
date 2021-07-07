from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    titulo = models.CharField("titulo", max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    


