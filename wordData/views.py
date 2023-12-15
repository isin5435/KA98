from django.shortcuts import render
from .models import Word, DestinationVocabulary
from rest_framework.views import APIView
from django.shortcuts import redirect

# Create your views here.


def word_list(request):
    words = Word.objects.all()
    context = {'words': words}
    return render(request, 'Project/Word.html', context)

    def __str__(self):
        return self.subject

class WordView(APIView):
    def get(self,request):
        return render(request, 'Project/Word.html')
    

def transfer_vocabulary(request):
    if request.method == 'POST':
        vocabularies = Word.objects.all()

        for vocab in vocabularies:
            DestinationVocabulary.objects.create(
                word=vocab.word,
                pronunciation=vocab.pronunciation,
                definition=vocab.definition,
                example=vocab.example
            )
        return redirect('Project/Home.html')

    return redirect('Project/Home.html')    