from django.contrib import admin
from django.urls import path, re_path, include

from .views import top as dais_top
from .views import new as dais_new
from .views import submit as dais_submit
from .views import user as dais_user
from .views import login as dais_login

urlpatterns = [
    re_path(
        r'^top/$',
        dais_top,
        name='top'
    ),
    re_path(
        r'^new/$',
        dais_new,
        name='new'
    ),
    re_path(
        r'^submit/$',
        dais_submit,
        name='submit'
    ),
    re_path(
        r'^user/$',
        dais_user,
        name='user'
    ),
    re_path(
        r'^login/$',
        dais_login,
        name='login'
    ),
]
