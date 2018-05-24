from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_first_used = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def long_desc(self):
        return f'{self.name}: {self.description}'
