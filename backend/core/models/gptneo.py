from django.db import models


class GptNeo(models.Model):
    path = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.path
