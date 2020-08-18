from django.db import models

# Create your models here.


class Text_line(models.Model):
    Text = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Text}'
