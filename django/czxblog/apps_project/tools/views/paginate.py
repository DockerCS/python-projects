from django.core.paginator import Paginator  # django默认分页器
from django.conf import settings

# 分页器方法
def getPages(request, objectlist):
    """得到页码"""
    currentPage = request.GET.get('page', 1)
    paginator = Paginator(objectlist, settings.EACHPAGE_NUMBER)
    objectlist = paginator.page(currentPage)

    page_range = []
    current = objectlist.number  # 当前页码
    page_all = paginator.num_pages  # 总页数
    mid_pages = 3  # 中间段显示的页码数
    page_goto = 1  # 默认跳转的页码

    # 优化显示的页码列表
    if page_all <= 2 + mid_pages:
        # 页码少于六页就不需要隐藏
        page_range = paginator.page_range
    else:
        # 添加应该显示的页码
        page_range += [1, page_all]
        page_range += [current-1, current, current+1]

        # 如果当前页是首尾页，范围拓展多1页
        if current == 1 or current == page_all:
            page_range += [current+2, current-2]

        # 去掉重复的页码
        page_range = filter(lambda x: x>=1 and x<=page_all, page_range)

        # 排序去重
        page_range = sorted(list(set(page_range)))

        # 查漏补缺
        # 从第2个开始遍历，查看页码间隔，若间隔为0则是连续的
        # 若间隔为1则补上页码；间隔超过1，则补上省略号
        t = 1
        for i in range(len(page_range)-1):
            step = page_range[t] - page_range[t-1]
            if step >= 2:
                if step == 2:
                    page_range.insert(t, page_range[t]-1)
                else:
                    page_goto = page_range[t-1] + 1
                    page_range.insert(t, '...')
                t += 1
            t += 1

    # 优化之后的页码列表
    paginator.page_range_ex = page_range
    # 默认跳转页的值
    paginator.page_goto = page_goto

    return paginator, objectlist








