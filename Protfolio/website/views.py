from django.shortcuts import render


# Create your views here.


def index(request):
    context = {'title': 'Mizanur Rahman'}
    return render(request, 'index.html', context)