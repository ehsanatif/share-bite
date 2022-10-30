from django.db import models


class Modifiers(models.Model):
    description = models.TextField(max_length=300, unique=True, blank=False)

    def __str__(self):
        return str(self.id)
