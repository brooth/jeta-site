from django.shortcuts import render
from django.http import Http404

from .models import MarkdownPage


def markdown_page(request, path):
    try:
        model = MarkdownPage.objects.get(path=path)
    except MarkdownPage.DoesNotExist:
        raise Http404("Page " + path + " not found")

    content = {'content': model}
    return render(request, 'home/markdown_page.html', content)
