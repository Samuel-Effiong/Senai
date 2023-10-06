
from django.urls import path
from .views import ArticleView


urlpatterns = [
    path('<str:project_name>/', ArticleView.as_view(), name='articles')
]
