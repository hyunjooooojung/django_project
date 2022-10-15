from django.shortcuts import redirect
from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_detail, name="article_detail"),
    path('create_article/', views.create_article, name="create-article"),
]


