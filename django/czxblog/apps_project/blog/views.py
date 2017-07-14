from django.shortcuts import render, redirect, get_object_or_404
from ..blog.models import Article, Comment, Poll
from ..blog.forms import CommentForm
from ..user.forms import LoginForm

import markdown2

# 主页方法
def index(request):
    article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    context = {'article_list': article_list}
    return render(request, 'index.html', context)


# 文章的方法
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    content = markdown2.markdown(article.content, extras=["code-friendly", "fenced-code-blocks", "header-ids", "toc", "metadata"])
    commentform = CommentForm()
    loginform = LoginForm()
    comment = article.comment_set.all

    return render(request, 'article_page.html', {
        'article': article,
        'loginform': loginform,
        'commentform': commentform,
        'content': content,
        'comment': comment,
        })


# 评论方法
def comment(request, article_id):
    # if request.method == 'POST':

    pass



# 点赞方法
def poll(request):

    pass