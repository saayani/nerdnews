from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse

from resources.models import Link, Vote


def top(request):
    template = "top.html"
    news_items = Link.objects.all().values()

    for news_item in news_items:
        user_id = news_item.get('user_id')
        news_item['user'] = User.objects.get(id=user_id)
        news_item['score'] = Vote.objects.filter(
                link_id=news_item['id']).count()

    news_items = sorted(news_items, key=lambda k: k['score'], reverse=True)

    context = {
        'news_items': news_items,
        'top_active': True,
    }

    if request.user.is_authenticated:
        context['karma'] = 0

    return render(
        request,
        template_name=template,
        context=context,
    )


def new(request):
    template = "new.html"
    news_items = Link.objects.all()

    context = {
        'news_items': news_items,
        'new_active': True,
    }

    if request.user.is_authenticated:
        context['karma'] = 0


    return render(
        request,
        template_name=template,
        context=context,
    )


def submit(request):
    template = "submit.html"

    context = {
        'news_items': news_items,
        'submit_active': True,
    }

    if request.user.is_authenticated:
        context['karma'] = 0


    return render(
        request,
        template_name=template,
        context=context,
    )


def user(request):
    raise NotImplementedError


def upvote(request):
    if not request.user.is_authenticated:
        return JsonResponse({'vote': ''})

    _id = request.GET.get('item_id')
    if _id is None:
        return JsonResponse({'vote': ''})

    _id = int(_id)
    link = Link.objects.filter(id=_id).first()
    if link is None:
        return JsonResponse({'vote': ''})

    votes = Vote.objects.filter(link=link)
    has_voted = votes.filter(user=request.user)
    if has_voted:
        return JsonResponse({'vote': votes.count()})

    vote_obj = Vote(link=link, user=request.user)
    vote_obj.save()

    votes = votes.count()

    return JsonResponse({'vote': votes})


