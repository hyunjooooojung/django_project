from django.shortcuts import render, redirect
from django.http import HttpResponse
from community.models import Article
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-created_at')
    context = {
        'articles':articles
    }
    
    return render(request, 'index.html', context)

def create_article(request):
    if request.method == "GET":
        return render(request, 'create_article.html')
    
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Article.objects.create(title=title, content=content, user=user)
        return redirect('community:index')
    
    
def article_detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'article_detail.html', context) 


def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user == article.user:
        if request.method == "GET":
            context = {
            'article': article
            }
            return render(request, "update_article.html", context)
        elif request.method == "POST":
            # 방법 1
            # title = request.POST.get("title")
            # content = request.POST.get("content")
            # article.title = title
            # article.content = content
            # 방법 2
            article.title = request.POST.get("title")
            article.content = request.POST.get("content")
            # db에 저장 요청
            article.save()
            context = {
            'article': article
            }
            return redirect("community:article_detail",  article_id)
        


def delete_article(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        if request.user == article.user: 
            article.delete()
            return redirect("community:index")
