from django.db import models


class ContactMessage(models.Model):
    subject = models.CharField(max_length=200)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.subject}"
