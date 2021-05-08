from django.urls import path
from . import views

urlpatterns=[
    #path('<int:pk>/',views.single_post_page),
    #<int:pk>는 정수 형태의 값을 pk라는 변수로 담아 single_post_page() 함수로 넘기라는 의미
    #path('',views.index),
    path('update_post/<int:pk>/',views.PostUpdate.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('tag/<str:slug>/',views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]