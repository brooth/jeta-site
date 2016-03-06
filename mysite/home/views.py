from django.shortcuts import render

# Create your views here.
from .models import MarkdownPage


def markdown_page(request, path):
    try:
        model = MarkdownPage.objects.get(path=path)
    except Question.DoesNotExist:
        raise Http404("Page " + path + " not exist")

    content = {'content': model}
    return render(request, 'home/markdown_page.html', content)
