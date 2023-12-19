from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, 'Project/Home.html')

class Chapter(APIView):
    def get(self, request):
        return render(request, 'Project/chapter.html')

class Word(APIView):
    def get(self,request):
        return render(request, 'Project/Word.html')

class Userpage(APIView):
    def get(self,request):
        return render(request, 'Project/userPage.html')