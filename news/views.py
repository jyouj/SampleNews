from django.shortcuts import render
from django.views import generic
from django.conf import settings

from newsapi import NewsApiClient

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_top_headlines(country='jp')
        # print(context['top_headlines'])
        return context
