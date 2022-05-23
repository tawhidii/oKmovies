from django.db import models


class TimeStampedModel(models.Model):
    """ Model Definition for timestamped model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ar = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
