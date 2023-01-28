from django.db import models


class WikiKeys(models.Model):
    key = models.CharField(max_length=255, null=False)
    value = models.TextField(null=False, help_text="Source for wiki keys")

    def __str__(self):
        return self.key + self.value[:100]
