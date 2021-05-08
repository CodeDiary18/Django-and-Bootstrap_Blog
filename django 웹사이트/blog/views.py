from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):#기존 FBV의 index와 같은 역할
    model=Post  # 포스트 목록
    #template_name='blog/index.html'
    ordering='-pk' # 최신 포스트부터 정렬되어 나옴

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model=Post
    context_object_name='post' # 디폴트는 object
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category="미분류"
        post_list=Post.objects.filter(category=None)
    else:
        category=Category.objects.get(slug=slug)
        post_list=Post.objects.filter(category=category)
        
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories':Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category':category,
        }
    )
# def index(request):
#     posts=Post.objects.all().order_by('-pk') #모든 포스트 레코드 가져와서 posts에 저장
#                                              #order_by('-pk') : pk의 역순으로 정렬 -> 최신 포스트부터 노출

#     return render(
#         request,
#         'blog/index.html',
#         { #포스트를 딕셔너리 형태로 추가한 것
#             'posts':posts,
#         }
#     )
# def single_post_page(request, pk):
#     post=Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )