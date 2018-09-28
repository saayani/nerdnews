from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import JsonResponse
from django import forms

from resources.models import Link, Vote
from dais.forms import SignupForm, SubmitForm

import tldextract


def redirect_homepage(request):
    return HttpResponseRedirect(reverse('top'))


def top(request, page=1):
    template = "top.html"
    news_items = Link.objects.all().values()

    for news_item in news_items:
        user_id = news_item.get('user_id')
        news_item['user'] = User.objects.get(id=user_id)
        news_item['score'] = Vote.objects.filter(
                link_id=news_item['id']).count()

    news_items = sorted(news_items, key=lambda k: k['score'], reverse=True)

    # Working on the Pagination for the first time. Learnt from here
    # https://docs.djangoproject.com/en/dev/topics/pagination/#example
    p = Paginator(news_items, 10)
    page_num = p.page(page)
    news_items = page_num.object_list
    has_next = page_num.has_next()
    has_prev = page_num.has_previous()
    num_pages = p.num_pages
    prev_page = page - 1
    next_page = page + 1


    context = {
        'news_items': news_items,
        'top_active': True,
        'num_pages': num_pages,
        'has_prev': has_prev,
        'has_next': has_next,
        'prev_page': prev_page,
        'next_page': next_page,
        'page': page
    }

    if request.user.is_authenticated:
        context['karma'] = 0

    return render(
        request,
        template_name=template,
        context=context,
    )


def new(request, page=1):
    template = "new.html"

    news_items = Link.objects.all().order_by('-timestamp').values()

    # Working on the Pagination for the first time. Learnt from here
    # https://docs.djangoproject.com/en/dev/topics/pagination/#example
    p = Paginator(news_items, 10)
    page_num = p.page(page)
    news_items = page_num.object_list
    has_next = page_num.has_next()
    has_prev = page_num.has_previous()
    num_pages = p.num_pages
    prev_page = page - 1
    next_page = page + 1

    for news_item in news_items:
        user_id = news_item.get('user_id')
        news_item['user'] = User.objects.get(id=user_id)
        news_item['score'] = Vote.objects.filter(
                link_id=news_item['id']).count()

    context = {
        'news_items': news_items,
        'new_active': True,
        'num_pages': num_pages,
        'has_prev': has_prev,
        'has_next': has_next,
        'prev_page': prev_page,
        'next_page': next_page,
        'page': page
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

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data['title']
            url = cleaned_data['url']

            link = Link.objects.filter(user=request.user, url=url)
            if not link:

                parsed_url = tldextract.extract(url)
                host = '.'.join([parsed_url.domain, parsed_url.suffix])

                link_obj = Link(
                    title=title, url=url, user=request.user, host=host)
                link_obj.save()
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like this link exists')
    else:
        form = SubmitForm()
    return render(request, 'submit.html', {'form' : form})

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


def signup(request):
    template = "signup.html"

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('top'))

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (
                User.objects.filter(username=username).exists() or
                User.objects.filter(email=email).exists()):

                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError(
                     'Looks like a username with that email'
                     'or password already exists'
                )
    else:
        form = SignupForm()
    return render(request, template, {'form' : form})
