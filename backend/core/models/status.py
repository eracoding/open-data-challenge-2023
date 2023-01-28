from django.db import models


class Status(models.Model):
    status = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.status

