from django.db import models
from django.urls import reverse


class Snack(models.Model):
    name = models.CharField(max_length=200)
    purchaser= models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    description = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('snack_list')

    def __str__(self):
        return self.name
