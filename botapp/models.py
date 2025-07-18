from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} ({self.username})"