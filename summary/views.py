from django.shortcuts import redirect, render
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

""" import spacy 
nlp = spacy.load('en')
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest """

#from spacy_textsummarizer import text_summarizer
from nltk_textsummarizer import nltk_summarizer

# Create your views here.
def home(request):
    return render(request, 'summary/home.html')

def summary(request):
    return render(request, 'summary/summary.html')

def summarizeText(request):
    if request.method == 'POST':
        rawtext = request.POST['text']
        summary = nltk_summarizer(rawtext)
        data = {
            'rawtext':rawtext,
            'summary':summary,
        }
        return render(request, 'summary/result.html', data)

def summarizeUrl(request):
    if request.method == 'POST':
        try:
            url = request.POST['url']
            page = urlopen(url)
            soup = BeautifulSoup(page, features = 'html.parser')
            rawtext = ' '.join(map(lambda p:p.text,soup.find_all('p')))
            summary = nltk_summarizer(rawtext)
            data = {
            'rawtext':rawtext,
            'summary':summary,
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
        summary = nltk_summarizer(rawtext)
        data = {
            'rawtext':rawtext,
            'summary':summary,
        }
        return render(request, 'summary/result.html', data)

def learn(request):
    return render(request, 'summary/learn.html')