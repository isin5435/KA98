from django.shortcuts import render
from .models import Word, UserVocabulary
from rest_framework.views import APIView
from django.shortcuts import redirect
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
