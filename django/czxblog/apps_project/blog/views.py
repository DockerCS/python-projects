from django.shortcuts import render, get_object_or_404
from apps_project.tools.decorator.views_decorator import record_view
from ..blog.models import Article, Category
from ..tools.views.article_recommend import rand_article, pre_next_article
from ..tools.views.paginate import getPages


# from ..user.forms import LoginForm

# 主页方法
def index(request):
    article_list = Article.objects.query_by_time()
    pages, article_list = getPages(request, article_list)

    data = {}
    data["article_list"] = article_list
    data["pages"] = pages
    data['rand_articles'] = rand_article()  # 主页随机推荐文章
    # loginform = LoginForm()

    return render(request, 'index.html', data)

# 文章分类
def blog_catergory(request, category_id):
    categorys = Category.objects.all()
    blog_filter_list = Article.objects.query_by_category(category_id)
    pages, blog_filter_list = getPages(request, blog_filter_list)


    data = {}
    data['categorys'] = categorys
    data['blog_filter_list'] = blog_filter_list
    data['pages'] = pages
    data['rand_articles'] = rand_article()  # 博客筛选页随机推荐文章
    return render(request, 'blog/blog_category_page.html', data)

# 文章详情页的方法
@record_view(Article)
def article_detail_show(request, id):
    data = {}
    data['article'] = get_object_or_404(Article, id=id)
    data['content'] = data['article'].content
    data['rand_articles'] = rand_article(id)  # 加入id，并把id传入article_recommend以便排除正在浏览的文章
    data['pre_article'] = pre_next_article(id)[0]  # 代表引用pre_next_article方法返回的第一个参数
    data['next_article'] = pre_next_article(id)[1]  # 代表引用pre_next_article方法返回的第二个参数

    # commentform = CommentForm()
    # loginform = LoginForm()
    # comment = article.comment_set.all
    return render(request, 'blog/article_detail_page.html', data)

# 评论方法
def comment(request, article_id):
    # if request.method == 'POST':

    pass
