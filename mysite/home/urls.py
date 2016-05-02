
from django.conf.urls import url
from django.views.generic import TemplateView

from django.contrib.sitemaps.views import sitemap
from home.models import MarkdownPageSitemap, StaticSitemap

from . import views


sitemaps = {
    'posts': MarkdownPageSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^donate\.html$', TemplateView.as_view(template_name='home/donate.html')),
    url(r'^(?P<path>.*)$', views.markdown_page),
]
