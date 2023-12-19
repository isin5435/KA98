from django.shortcuts import render
from django.http import JsonResponse
import requests
from crawl.models import Words
# Create your views here.

def search_word(request):
    word = request.GET.get('word')
    result = Words.objects.filter(text=word).first()
    if result:
        return JsonResponse({'word': result.text, 'meaning': result.definitions})
    
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = response.json()
    if isinstance(data, list) and 'meanings' in data[0]:
        for item in data:
            meaning = item['meanings'][0]
            definitions = meaning['definitions'][0]
            definition = definitions['definition']
            return JsonResponse({'word': word, 'meaning': definition})
    else:
        return JsonResponse({'word': "No word information in DataBase", 'meaning': ""})

