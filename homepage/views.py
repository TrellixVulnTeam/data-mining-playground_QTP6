from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html', {})

def k_means(request):
    return render(request, 'homepage/k_means.html', {})


