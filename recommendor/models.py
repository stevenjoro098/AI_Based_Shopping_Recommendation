from django.db import models

# Create your models here.
class UserPreference(models.Model):
    user_id = models.IntegerField(unique=True)
    preferred_categories = models.JSONField()

    def __str__(self):
        return f"User { self.user_id } Preferences"