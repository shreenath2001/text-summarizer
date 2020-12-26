from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'summary/home.html')

def summary(request):
    return render(request, 'summary/summary.html')

def learn(request):
    return render(request, 'summary/learn.html')
