from django.db import models
from django.contrib.auth.models import User

class Link(Base):
    title = models.Charfield('title', max_length=255, blank=True)
    url = models.URLField('URL', max_length=200, blank=True)
    text = models.TextField('text', max_length=255, blank=True)
    user = models.ForeignKey(User)

class Vote(models.Model):
    user = models.ForeignKey(User)
    link =  models.ForeignKey(Link)


