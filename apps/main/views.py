from django.shortcuts import render


def index_page(request):
    context = {}
    return render(request, 'main/index.html', context)
