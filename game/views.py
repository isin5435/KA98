from django.shortcuts import render
from rest_framework.views import APIView
from wordData.models import Word
import random
from django.http import JsonResponse
# Create your views here.

class game(APIView):
    def get(self, request):
        return render(request, 'Project/game.html')


def get_definitions(request):
    words = Word.objects.all()
    random_words = random.sample(list(words),25)
    word_definitions = [{"word" : word.word, "definition": word.definition} for word in random_words]
    return JsonResponse({'definitions':word_definitions})
    

