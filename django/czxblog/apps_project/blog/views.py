from django.shortcuts import render, redirect, get_object_or_404
from ..blog.models import Article, Comment
from ..blog.forms import CommentForm
from ..tools.views.paginate import getPages
from ..tools.views.view_decorator import record_view
from ..tools.views.article_recommend import rand_article, pre_next_article
# from ..user.forms import LoginForm

import markdown2

# 主页方法
def index(request):
    article_list = Article.objects.query_by_time()
    pages, article_list = getPages(request, article_list)

    data = {}
    data["article_list"] = article_list
    data["pages"] = pages
    data['rand_articles'] = rand_article()
    # loginform = LoginForm()

    return render(request, 'index.html', data)

# 文章的方法
@record_view(Article)
def article_show(request, id):
    data = {}
    data['article'] = get_object_or_404(Article, id=id)
    data['content'] = markdown2.markdown(data['article'].content, extras=["code-friendly", "fenced-code-blocks", "header-ids", "toc", "metadata"])
    data['rand_articles'] = rand_article(id)  # 加入id，并把id传入article_recommend以便排除正在浏览的文章
    data['pre_article'] = pre_next_article(id)[0]
    data['next_article'] = pre_next_article(id)[1]

    # commentform = CommentForm()
    # loginform = LoginForm()
    # comment = article.comment_set.all

    return render(request, 'blog/article_page.html', data)

# 评论方法
def comment(request, article_id):
    # if request.method == 'POST':

    pass

# 点赞方法
def poll(request):

    pass