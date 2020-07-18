from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'learn/index.html')


def education(request):
    return render(request, 'learn/page10.html')

# def preloader(request):
#     return render(request, 'learn/preloader.html')


# def team(request):
    # return render(request, 'learn/team.html')


def article(request):
    return render(request, 'learn/page2.html')

def mindPuzzle(request):
    return render(request, 'learn/page9.html')


def services(request):
    return render(request, 'learn/page3.html')


# def techmagic(request):
#     return render(request, 'learn/page4.html')


def contact(request):
    return render(request, 'learn/page5.html')


# def software(request):
#     return render(request, 'learn/page6.html')


# page - 7 missing


def training(request):
    return render(request, 'learn/page8.html')
