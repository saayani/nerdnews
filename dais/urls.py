from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include

from dais import views

urlpatterns = [
    re_path(
        r'^top/$',
        views.top,
        name='top'
    ),
    path(
        r'top/<int:page>/',
        views.top,
        name='top'
    ),
    re_path(
        r'^new/$',
        views.new,
        name='new'
    ),
    re_path(
        r'^submit/$',
        views.submit,
        name='submit'
    ),
    re_path(
        r'^user/$',
        views.user,
        name='user'
    ),
    re_path(
        r'^login/$',
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"
    ),
    re_path(
        r'^signup/$',
        views.signup,
        name="signup"
    ),
    re_path(
        r'^logout/$',
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    re_path(
        r'^ajax/upvote/$',
        views.upvote,
        name="upvote"
    ),
    re_path(
        r'^$',
        views.redirect_homepage,
        name="redirect"
    ),

]
