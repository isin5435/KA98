from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import Words

word_list = []

def wordcrawl(request):
    #크롤링 주소
    url = 'https://www.graduateshotline.com/gre-word-list.html#x2'

    req = requests.get(url)

    #전체 페이지 html 가지고 오기
    soup = BeautifulSoup(req.text, 'html.parser')

    #태그 가져오기
    words = soup.find('table').findAll('a')

    for word in words:
        word_list.append(word.text)
    
    return HttpResponse('word 배열 생성완료')

def printword(request):
    
    words = Words.objects.all()
    html = "<ul>"

    for word in words:
        html += "<li>{}</li>".format(word.text)
    html += "</ul>"
    return HttpResponse(html)

def makewordbook(request):
    for word in word_list:
        Words.objects.create(text=word)
    return HttpResponse('단어 저장 완료')

def comp(request):
    urls = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    words = Words.objects.all()

    for word in words:
        url = urls + word.text
        response = requests.get(url)
        data = response.json()

        if isinstance(data, list) and 'meanings' in data[0]:

            for item in data:
                meaning = item['meanings'][0]
                definitions = meaning['definitions'][0]
                definition = definitions['definition']

                word.definitions = definition
                word.save()

    return HttpResponse('뜻 저장 완료')





# Create your views here.
