from django.shortcuts import render

# Create your views here.
def level1(request):
    return render(request,'level1.html')


def level2(request):
    return render(request,'demo2.html')


def level6(request):
    return render(request,'demo6.html')


def shop(request):
    return render(request,'shop1.html')