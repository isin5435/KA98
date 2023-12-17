from django.shortcuts import render
from .models import Word, UserVocabulary
from rest_framework.views import APIView
from django.shortcuts import redirect
from crawl.models import Words
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

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
        users = User.objects.all()
        for user in users:
            for vocab in vocabularies:
                UserVocabulary.objects.create(
                    user=user,  # Assuming 'user' is an instance of the User model
                    vocabulary=vocab  # Assuming 'vocab' is an instance of the Vocabulary model
                )
        return redirect('Project/Home.html')
    return redirect('Project/Home.html') 


def userWordlist(request):
    userWords = UserVocabulary.objects.all()
    context = {'userWords': userWords}
    return render(request, 'Project/userPage.html', context)
