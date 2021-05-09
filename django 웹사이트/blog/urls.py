from django.urls import path
from . import views

urlpatterns=[
    #path('<int:pk>/',views.single_post_page),
    #<int:pk>는 정수 형태의 값을 pk라는 변수로 담아 single_post_page() 함수로 넘기라는 의미
    #path('',views.index),
    path('search/<str:q>/',views.PostSearch.as_view()),
    path('update_comment/<int:pk>/',views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/',views.delete_comment),
    path('update_post/<int:pk>/',views.PostUpdate.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('tag/<str:slug>/',views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/',views.new_comment),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]