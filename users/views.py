from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.shortcuts import get_object_or_404

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html/')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return render(request, 'login.html')
        else:
            return HttpResponse("비밀번호 확인 틀렸습니다.")
    
    else:
        return HttpResponse("허용되지 않은 메소드입니다.")
    
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html/')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            # 로그인 성공하면 index 페이지로 이동
            return redirect('community:index')
        else:
            # Redirect to a success page.
            return HttpResponse("로그인 실패.")
                        
                        
# def user(request):
#     return HttpResponse(request.user)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    for article in user.article_set.all():
        print(article)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)