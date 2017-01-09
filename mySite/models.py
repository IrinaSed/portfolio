from datetime import date, datetime

from django.db import models

from mySite.utils import get_user_ip, get_user_agent


class Visit(models.Model):
    ip = models.CharField(max_length=15)
    page = models.CharField(max_length=10)
    user_agent = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now=True)

    @staticmethod
    def make(request, page):
        Visit.objects.create(
            ip=get_user_ip(request),
            page=page,
            user_agent=get_user_agent(request)
        )

    @staticmethod
    def all_count():
        return Visit.objects.count()

    @staticmethod
    def today_count():
        return Visit.objects.filter(created__gt=date.today()).count()

    @staticmethod
    def get_last_visit_of(page, user_ip):
        try:
            return Visit.objects.filter(
                ip=user_ip, page=page
            ).order_by('-id')[1].created
        except IndexError:
            return datetime.now()


class Comment(models.Model):
    message = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_new_created(last_update):
        return list(map(dict, Comment.objects.filter(created__gt=last_update).values()))

    @staticmethod
    def make(form):
        Comment.objects.create(
            message=form.cleaned_data['message'],
            username=form.cleaned_data['username']
        )
        return {'username': form.cleaned_data['username'], 'message': form.cleaned_data['message'],}


class Like(models.Model):
    ip = models.CharField(max_length=15)
    anchor_image = models.CharField(max_length=100)

    @staticmethod
    def make(anchor, ip):
        if not Like.objects.filter(anchor_image=anchor, ip=ip).exists():
            Like.objects.create(
                anchor_image=anchor,
                ip=ip
            )

    @staticmethod
    def get_count(anchor):
        return Like.objects.filter(anchor_image=anchor).count()
