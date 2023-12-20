from django.shortcuts import render
from .models import Word, UserVocabulary
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
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