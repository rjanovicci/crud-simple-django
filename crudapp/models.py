from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 100, null = False)
    email = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return self.name
