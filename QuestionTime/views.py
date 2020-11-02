from django.shortcuts import render
from django.http import HttpResponse


def IndexTemplateView(request):
    return render(request, "demo/index.html")
