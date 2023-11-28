from django.db import models


class CodeSubmission(models.Model):
    content = models.TextField()
