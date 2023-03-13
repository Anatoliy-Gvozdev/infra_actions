from django.http import HttpResponse


def index(request):
    return HttpResponse('А это первая страница!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
