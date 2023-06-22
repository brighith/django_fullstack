from django.db import models

from log_reg_app.models import User


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE, blank=True, null=True)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    message = models.ForeignKey(
        Message, related_name="comments_message", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, related_name="comments_user",
                             on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
