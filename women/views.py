from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница положения women.")
def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям<h1><p>{catid}</p>")
def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам<h1><p>{year}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Такой страницы нет(((</p>")

