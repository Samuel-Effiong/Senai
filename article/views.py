from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import Article
# Create your views here.


COMPANY_NAME = 'SENAI'


class ArticleView(TemplateView):

    def setup(self, request, *args, **kwargs):
        super(ArticleView, self).setup(request, args, kwargs)
        self.template_name = f"articles/children/{kwargs['project_name']}.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)

        article = get_object_or_404(Article, slug=kwargs['project_name'])

        context['data'] = article
        context['company_name'] = COMPANY_NAME

        return context
