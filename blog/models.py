from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200)
    authour = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()

    def _str_(self):
        return self.title