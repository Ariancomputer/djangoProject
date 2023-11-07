from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    print(amount)
    return render(request, 'counter.html', {'amount': amount})
