from django.db import models


class Sections(models.Model):
    section_name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.TextField(max_length=300)

    def __str__(self):
        return str(self.section_name)
