from django.shortcuts import render


def top(request):
    template = "top.html"

    context = {}

    return render(
        request,
        template_name=template,
        context=context,
    )


def new(request):
    raise NotImplementedError


def submit(request):
    raise NotImplementedError


def user(request):
    raise NotImplementedError


def login(request):
    raise NotImplementedError
