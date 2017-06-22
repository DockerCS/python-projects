from django.shortcuts import render
from blog.models import Article, Comment, Poll, User

def index(request):
    article_list = Article.objects.query_by_time()
    # loginform = LoginForm()
    context = {'article_list': article_list}
    return render(request, 'index.html', context)
# Create your views here.
