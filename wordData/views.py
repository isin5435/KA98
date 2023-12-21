from django.shortcuts import render
from .models import Word, UserVocabulary
from rest_framework.views import APIView
from django.shortcuts import redirect
from crawl.models import Words
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def word_list(request):
    word = Word.objects.all()
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
        word_id = request.POST.get('id')
        vocabulary = Word.objects.get(id=word_id)

        UserVocabulary.objects.create(
            user=request.user,  # Assuming 'user' is an instance of the User model
            vocabulary=vocabulary  # Assuming 'vocab' is an instance of the Vocabulary model
        )
        return redirect('word')
    return redirect('word') 


def userWord_list(request):
    user_id = request.user.id
    userWords = UserVocabulary.objects.filter(user_id = user_id)
    context = {'userWords': userWords}
    return render(request, 'Project/userPage.html', context)


def delete_word(request, vocab_id):
    vocab = UserVocabulary.objects.filter( id=vocab_id)  # Adjust the model name as necessary
    vocab.delete()
    return redirect('userPage')  # Redirect to the view that shows the list