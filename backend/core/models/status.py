from django.db import models


class Status(models.Model):
    status = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.id)
