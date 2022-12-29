from django.views.generic import TemplateView
from data_analysis.models import DataAnalysis

# Create your views here.


COMPANY_NAME = "SENAI"


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        data_analysis = DataAnalysis.objects.all()

        context['company_name'] = COMPANY_NAME
        context['data_analysis'] = data_analysis

        return context
