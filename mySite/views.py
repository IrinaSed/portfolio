from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def gallery(request):
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
    return render(request, 'info.html')
