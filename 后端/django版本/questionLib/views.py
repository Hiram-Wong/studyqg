from django.shortcuts import render
from . import models

# Create your views here.
from questionLib.common.utils import json_response
from django.db.models import Q
from django.http import HttpResponse


def hello(request):
    return json_response(200, "hello word", [])


def banner(request):
    res = models.Banner.objects.all()
    list = []
    for i in res:
        data = {
            'id': i.id,
            'type': i.type,
            'url': i.url
        }
        list.append(data)
    # print(res)
    return json_response(200, "获取成功", list)
    # return HttpResponse(list)


def search(request):
    keyword = request.GET.get('kw')
    # res = models.QuestionLib.objects.filter(question__icontains=keyword)
    res = models.QuestionLib.objects.filter(
        Q(question__icontains=keyword) | Q(A__icontains=keyword) | Q(B__icontains=keyword) | Q(
            C__icontains=keyword) | Q(D__icontains=keyword))
    list = []
    for i in res:
        answer = i.answer
        if answer == 'A':
            answer_detail = answer + ":" + i.A
        elif answer == "B":
            answer_detail = answer + ":" + i.B
        elif answer == "C":
            answer_detail = answer + ":" + i.C
        else:
            answer_detail = answer + ":" + i.D
        data = {
            'id': i.id,
            'question': i.question,
            'answer': answer,
            'A': i.A,
            'B': i.B,
            'C': i.C,
            'D': i.D,
            'answer_detail': answer_detail
        }
        list.append(data)
    return json_response(200, "获取成功", list)


def id(request):
    id = request.GET.get('id')
    res = models.QuestionLib.objects.get(pk=id)
    data = {
        'id': res.id,
        'question': res.question,
        'answer': res.answer,
        'A': res.A,
        'B': res.B,
        'C': res.C,
        'D': res.D,
    }
    return json_response(200, "获取成功", data)


def log(request):
    res = models.Log.objects.all()
    list = []
    for i in res:
        data = {
            'versation': i.versation,
            'time': i.time,
            'description': i.description
        }
        list.append(data)
    return json_response(200, "获取成功", list)


def basic(request):
    res = models.QuestionLib.objects.all()
    question_total = len(res)
    res = models.Log.objects.all()
    versation = res.last().versation
    data = {
        'question_total': question_total,
        'versation': versation
    }
    return json_response(200, "获取成功", data)
