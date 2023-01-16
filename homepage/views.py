
from itertools import zip_longest
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http.response import JsonResponse

from data_analysis.models import DataAnalysis
from article.models import Article

# Create your views here.


COMPANY_NAME = "SENAI"


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        data_analysis = DataAnalysis.objects.all()
        articles = Article.objects.all()

        context['company_name'] = COMPANY_NAME

        portfolios = zip_longest(data_analysis, articles)
        context['portfolio'] = portfolios

        context['data_analysis'] = data_analysis
        context['articles'] = articles

        return context


class SendEmails(TemplateView):

    def post(self, request, *args, **kwargs):

        body = request.POST

        name = body['name']
        email = body['email']
        subject = body['subject']
        message = f"{subject}\n\n{body['message']}\n\n {email}"

        try:
            send_mail(subject=name, message=message, from_email=email,
                      recipient_list=[email])
        except Exception as e:
            return JsonResponse({'confirm': False})
        else:
            return JsonResponse({'confirm': True})

