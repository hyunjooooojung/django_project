from django.http import HttpResponse
from django.shortcuts import render
from .models import User

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
            return HttpResponse("회원가입 완료")
        else:
            return HttpResponse("비밀번호 확인 틀렸습니다.")
    
    else:
        return HttpResponse("허용되지 않은 메소드입니다.")
