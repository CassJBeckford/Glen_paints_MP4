from django.db import models


class faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.question
