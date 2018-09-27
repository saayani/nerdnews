from django.shortcuts import render

from resources.models import Link


def top(request):
    template = "top.html"
    news_items = Link.objects.all()

    context = {
        'news_items': news_items
    }

    return render(
        request,
        template_name=template,
        context=context,
    )


def new(request):
    template = "new.html"
    news_items = Link.objects.all()

    context = {
        'news_items': news_items
    }

    return render(
        request,
        template_name=template,
        context=context,
    )


def submit(request):
    template = "submit.html"

    context = {
        'news_items': news_items
    }

    return render(
        request,
        template_name=template,
        context=context,
    )


def user(request):
    raise NotImplementedError


def login(request):
    raise NotImplementedError
