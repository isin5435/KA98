from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import redirect
from functools import wraps

class Main(APIView):
    def get(self, request):
        return render(request, 'Project/index.html')

class Chapter(APIView):
    def get(self, request):
        return render(request, 'Project/chapter.html')

class Word(APIView):
    def get(self,request):
        return render(request, 'Project/Word.html')
    
class exam(APIView):
    def get(self, request):
        return render(request, 'Project/exam.html')
    
def login_required_or_redirect_home(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')  # You need to define HOME_URL in your settings
        return view_func(request, *args, **kwargs)
    return _wrapped_view