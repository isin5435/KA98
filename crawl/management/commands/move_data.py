from django.core.management.base import BaseCommand
from crawl.models import Words
from wordData.models import Word

class Command(BaseCommand):
    help = 'Move word from Crawl_words to wordData_word'

    def handle(self, *args, **options):
        cwords = Words.objects.all()

        for cwords in cwords:
            wword = Word()
            wword.word = cwords.word
            wword.definition = cwords.definition
            wword.pronunciation = ""
            wword.example = ""
            wword.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully moved data'))