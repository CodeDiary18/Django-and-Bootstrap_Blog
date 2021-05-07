from django.shortcuts import render
from .models import Post

def index(request):
    posts=Post.objects.all().order_by('-pk') #모든 포스트 레코드 가져와서 posts에 저장
                                             #order_by('-pk') : pk의 역순으로 정렬 -> 최신 포스트부터 노출

    return render(
        request,
        'blog/index.html',
        { #포스트를 딕셔너리 형태로 추가한 것
            'posts':posts,
        }
    )
