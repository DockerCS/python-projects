"""文章随机推荐和定向推荐"""
from apps_project.blog.models import Article

# 随机推荐文章
def rand_article(except_id=0):
    """
    随机推荐文章，默认推荐十篇文章，并且排除现在在看的这一篇
    在blog应用中引用rand_article方法：data['rand_articles'] = rand_article(),
    再由其传去前端
    """
    rand_num = 10
    return Article.objects.exclude(id=except_id).order_by('?')[:rand_num]
