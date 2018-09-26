from django.contrib import admin
from .models import Link, Vote


class LinkAdmin(admin.ModelAdmin):
    """ Register Link model in Admin """
    pass
admin.site.register(Link, LinkAdmin)


class VoteAdmin(admin.ModelAdmin):
    """ Register Vote model in Admin"""
    pass
admin.site.register(Vote, VoteAdmin)
