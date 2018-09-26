from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    """ Abstract model to save the common data """
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Link(Base):
    """ Model to save the link information """
    title = models.CharField('title', max_length=255, blank=True)
    url = models.URLField('URL', max_length=200, blank=True)
    text = models.TextField('text', max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Vote(models.Model):
    """ Model to save the vote on a link Item """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link =  models.ForeignKey(Link, on_delete=models.CASCADE)


