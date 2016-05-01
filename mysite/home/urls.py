
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^donate.html', TemplateView.as_view(template_name='home/donate.html')),
    url(r'^(?P<path>.*)$', views.markdown_page),
]
