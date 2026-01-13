from django.db import models

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.message[:30]} {self.created_at}"