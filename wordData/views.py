from django.shortcuts import render
from .models import Word, DestinationVocabulary
from rest_framework.views import APIView
from django.shortcuts import redirect
from crawl.models import Words
from django.contrib.auth.views import LoginView

# Create your views here.


def word_list(request):
    word = Words.objects.all()
    return render(request, 'Project/Word.html', {'words': word})

    def __str__(self):
        return self.subject

class WordLoginView(LoginView):
    template_name = 'Project/Word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = Words.objects.all()
        return context
    

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