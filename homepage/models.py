from django.db import models

# Create your models here.


class Text_line(models.Model):
    user_text = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_text}'
