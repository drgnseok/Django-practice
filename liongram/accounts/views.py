from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

from posts.models import User

from.forms import UserCreateForm, SignUpForm


def signup_view(request):
    #GET요청시 HTML 응닫
    if request.method =='GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        #POST 요청 시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)

        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            #redirect
            return redirect('accounts:signup')

def login_view(request):
    #GET요청시 HTML 응닫
    if request.method =='GET':
        #로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        #데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            #비즈니스 로직 처리 -  로그인 처리
            login(request, form.user_cache) #비즈니스 로직 처리
            #응닫
            return redirect('index')
        else:
            #응답
            return render(request, 'accounts/login.html', {'form' : form})
        

def logout_view(request):
    if request.user.is_authenticated:# 로그인일때
        logout(request)
    
    # 비즈니스 로직 처리 - 로그아웃
    # 응답
    return redirect('index')

        #password = request.POST.get('password')
        #password 에 대한 유효성검사~~~

        # 데이터 유효성 섬감 (is_valid())
        # 비즈니스 로직 처리
        # 출력
        