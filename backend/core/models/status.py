from django.db import models


class Status(models.Model):
    status = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.id)

    def learn(self):
        self.status = 1
        self.save()

    def finish(self):
        self.status = 2
        self.save()

    def no_work(self):
        self.status = 0
        self.save()
