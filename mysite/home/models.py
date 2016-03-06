from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
from markdown import markdown


class MarkdownPage(models.Model):
    title = models.CharField(max_length=140)
    path = models.CharField(max_length=140, unique=True, blank=True)
    md_filename = models.CharField(max_length=100)
    html_content = models.TextField(editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        md_file = open(settings.MARKDOWN_FILES_URL + self.md_filename, 'r+')
        self.html_content = markdown(md_file.read(), ['codehilite'])
        md_file.close()
        super(MarkdownPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.md_filename + ' at /' + self.path
