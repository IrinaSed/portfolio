import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from mySite.forms import CommentForm
from mySite.gen_image import get_counter_image, get_like_image
from mySite.models import Visit, Comment, Like
from mySite.utils import get_user_ip


def index(request):
    Visit.make(request, '/')
    return render(request, 'index.html')


def gallery(request):
    Visit.make(request, '/gallery')
    images = [
        ('#ekb', 'ekb', 'images/ekb.jpg', 'images/ekb_tn.jpg'),
        ('#bonfire', 'bonfire', 'images/bonfire.jpg', 'images/bonfire_tn.jpg'),
        ('#hightEkb', 'hightEkb', 'images/hightEkb.jpg', 'images/hightEkb_tn.jpg'),
        ('#mat-mex', 'mat-mex', 'images/mat-mex.jpg', 'images/mat-mex_tn.jpg'),
        ('#konfuzy', 'konfuzy', 'images/konfuzy.jpg', 'images/konfuzy_tn.jpg'),
        ('#karacul', 'karacul', 'images/karacul.jpg', 'images/karacul_tn.jpg')
    ]
    return render(request, 'gallery.html', context={
        'images': images
    })


def info(request):
    Visit.make(request, '/info')
    return render(request, 'info.html')


def comment(request):
    Visit.make(request, '/comment')
    if request.method == 'POST' and request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            response_data = Comment.make(form)
            return JsonResponse(response_data)
    return render(request, 'comment.html', context={
        'comments': Comment.objects.all(),
        'form': CommentForm
    })


def like(request):
    if request.method == 'GET' and request.GET.get('what'):
        response = HttpResponse(content=get_like_image(
            request.GET.get('anchor')
        ).read())
        response['Content-Type'] = 'image/png'
        response['Content-Disposition'] = 'attachment;filename=counter.png'
        return response
    elif request.method == 'GET' and request.is_ajax():
        Like.make(request.GET.get('anchor'), get_user_ip(request))
        return HttpResponse('OK')


def visits(request):
    Visit.make(request, '/visits')
    response = HttpResponse(content=get_counter_image(
        request.GET.get('path'),
        get_user_ip(request),
    ).read())
    response['Content-Type'] = 'image/png'
    response['Content-Disposition'] = 'attachment;filename=counter.png'
    return response


def visit(request):
    Visit.make(request, '/visit')
    return render(request, 'visit.html', context={
        'visits': Visit.objects.all(),
    })


def comments_update(request):
    if request.method == 'GET' and request.is_ajax():
        last_update = datetime.datetime.fromtimestamp(int(request.GET.get('sync_time')) / 1e3)
        last = Comment.get_new_created(last_update)
        return JsonResponse({'new': last})
