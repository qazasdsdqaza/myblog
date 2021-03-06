from django.shortcuts import render, get_object_or_404
from blog.models import Blog, BlogType, Comment, Pic
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import QueryDict
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from user.models import User

ret = [{'code': 1000, 'msg': 'OK'},
       {'code': 1001, 'msg': '请求异常'},
       {'code': 1002, 'msg': '密码不一致'},
       {'code': 1003, 'msg': '用户名或密码不能为空'},
       {'code': 1004, 'msg': '用户已存在'},
       {'code': 1005, 'msg': '评论为空'},
       {'code': 1006, 'msg': '用户名或密码错误'},
       {'code': 1007, 'msg': '不能留空'},
       {'code': 1008, 'msg': '长度不符合要求, 请重新输入用户名或密码'},
       {'code': 1009, 'msg': '验证未通过'},
       ]


def paginator_(request, object_list):
    context = dict()
    #  分页器
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, 5)
    page_range = paginator.page_range
    context['current_page'] = current_page
    context['page_range'] = page_range
    try:
        page = paginator.page(current_page)
        context['page'] = page
        return context
    except Exception as e:
        page = paginator.page(1)
        context['page'] = page
        return context


def aside(request):
    context2 = dict()
    #  最新文章
    latest = Blog.objects.order_by('-created_time')[:5]
    #  归档
    blog_dates = Blog.objects.dates('created_time', 'day', order='ASC')
    #  分类
    blog_types = BlogType.objects.annotate(blog_count=Count('blog'))
    id_list = []
    for i in BlogType.objects.all():
        id_list.append(i.id)
    context2['latest'] = latest
    context2['blog_dates'] = blog_dates
    context2['blog_types'] = blog_types
    context2['id'] = id_list
    return context2


class BLogViewset(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class Index(APIView):
    def get(self, request):
        article = Blog.objects.all()
        blog_type = BlogType.objects.all()
        context = paginator_(request, article)
        context2 = aside(request)
        return render(request, 'index.html', locals())


class DetailPage(APIView):
    def get(self, request, article_id):
        context2 = aside(request)
        article = get_object_or_404(Blog, id=article_id)
        article.read_count += 1
        article.save()
        previous_blog = Blog.objects.filter(created_time__lt=article.created_time).last()
        next_blog = Blog.objects.filter(created_time__gt=article.created_time).first()
        if next_blog:
            next_id = next_blog.id
        if previous_blog:
            previous_id = previous_blog.id

        comment_list = Comment.objects.filter(article=article_id)
        return render(request, 'detail.html', locals())


class Archive(APIView):
    def get(self, request, year, month):
        blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
        context = paginator_(request, blogs_all_list)
        context2 = aside(request)
        return render(request, 'archive.html', locals())


class Category(APIView):
    def get(self, request, category_id):
        category_blog = Blog.objects.filter(blog_type=category_id)
        context = paginator_(request, category_blog)
        context2 = aside(request)
        return render(request, 'category.html', locals())


class Comments(APIView):
    def post(self, request, *args, **kwargs):
        article_id = request._request.POST['article_id']
        pid = request._request.POST['pid']
        content = request._request.POST['content']
        new_content = content.replace(' ', '')
        if new_content != '':
            comment_obj = Comment.objects.create(article_id=article_id, text=new_content,
                                                 parent_comment_id=pid, author=request.user.username)
            response = dict()
            response['created_time'] = comment_obj.created_time.strftime('%Y-%m-%d %X')
            response['username'] = request.user.username
            response['content'] = content
            response['comment_id'] = comment_obj.nid
            return JsonResponse(response)
        else:
            return JsonResponse(ret[8])

    def delete(self, request):
        comment_id = QueryDict(request._request.body)['comment_id']
        comment = Comment.objects.filter(nid=comment_id).first()
        if comment.author == request.user.username:
            comment.delete()
            return JsonResponse(ret[0])
        return JsonResponse(ret[1])


class AboutView(APIView):
    def get(self, request):
        return render(request, 'users/about.html')


def page_not_found(request, exception):
    return render(request, '404.html')



