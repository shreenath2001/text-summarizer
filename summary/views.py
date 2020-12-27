from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'summary/home.html')

def summary(request):
    return render(request, 'summary/summary.html')

def summarizeText(request):
    if request.method == 'POST':
        rawtext = request.POST['text']
        data = {
            'rawtext':rawtext,
        }
        return render(request, 'summary/result.html', data)

def summarizeUrl(request):
    if request.method == 'POST':
        try:
            url = request.POST['url']
            page = urlopen(url)
            soup = BeautifulSoup(page)
            rawtext = ' '.join(map(lambda p:p.text,soup.find_all('p')))
        except:
            rawtext = "Sorry, Unable to process!"
        data = {
            'rawtext':rawtext,
        }
        return render(request, 'summary/result.html', data)

def learn(request):
    return render(request, 'summary/learn.html')
