from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from wordData.models import Word
# Create your views here.

def exam(request):
    first_word = Word.objects.order_by('?').first()
    return render(request, 'Project/exam.html', {'word' : first_word})


def randon_word(request):
    word = Word.objects.order_by('?').first()
    return JsonResponse({'id' : word.id, 'definition' : word.definition})

def test_word(request, word_id):
    word = Word.objects.get(pk=word_id)
    answer = request.POST.get('answer', '')
    if word.word == answer:
        result = 'Correct!'
    else:
        result = 'Incorrect. The correct answer is ' + word.word
    return JsonResponse({'result': result})
