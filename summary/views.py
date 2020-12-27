from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image

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
            soup = BeautifulSoup(page, features = 'html.parser')
            rawtext = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            data = {
            'rawtext':rawtext,
        }
        except:
            problem = "Sorry, Unable to process!"
            data = {
                'problem':problem,
            }
        
        return render(request, 'summary/result.html', data)

def summarizeImage(request):
    if request.method == 'POST':
        image = request.FILES['image']
        fs = FileSystemStorage()
        imageName = fs.save(image.name, image)
        imageName = fs.url(imageName)
        loc = '.' + imageName
        img = Image.open(loc)
        rawtext = pytesseract.image_to_string(img)
        data = {
            'rawtext':rawtext,
        }
        return render(request, 'summary/result.html', data)

def learn(request):
    return render(request, 'summary/learn.html')
