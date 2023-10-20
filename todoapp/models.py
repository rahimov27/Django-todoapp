from django.db import models

# Create your models here.


class MessageModel(models.Model):
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Message"
