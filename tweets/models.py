import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key=True)
    # This could also be set to: null=True, on_delete=models.SET_NULL if we don't want to remove tweets with no user
    user    = models.ForeignKey(User, on_delete=models.CASCADE) # many users can have many tweets
    content = models.TextField(blank=True, null=True)
    image   = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }


# 2:49:28 33. Users & Tweets
# 2:57:09 34. Django Admin
