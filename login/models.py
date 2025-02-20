from django.db import models

class login(models.Model):
    user = models.CharField(max_length=100, null=False, blank=False)

    password = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"login [user={self.user}]"