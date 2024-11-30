from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm,LoginForm,FindUsernameForm,ResetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout

# 사용자 가입 /common/register 
# 사용자 아이디 찾기 /common/find_username
# 사용자 비밀번호 초기화 /common/reset_password
# 사용자 로그인 /common/login
# 사용자 로그아웃 /common/logout
# 사용자 정보 /common/profile
# 사용자 정보 수정 /common/update_profile
# 사용자 비밀번호 수정 /common/update_password/


# 사용자 가입
def common_register(request):
    # 입력폼 (비어있는 값
    # 처리
    if request.method == "POST":
        # 사용자가 입력한 데이터를 폼에 저장
        form = UserForm(request.POST)
        # 입력 폼 유효성 검사
        if form.is_valid():  # 통과가 되었다면 진행 
            user = User.objects.create_user(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
                email = form.cleaned_data["email"],
                first_name = form.cleaned_data["first_name"],
            )
            # 검사 성공
            user.save()  # DB에 저장
            messages.success(request,"회원가입이 완료되었습니다.")
            return redirect("common:login")
        else: 
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
            return render(request, "common/register.html",{"form":form})
    else:
        # 비어있는 폼 생성
        form = UserForm()
    return render(request, "common/register.html",{"form":form})

def common_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            # 사용자를 인증 시도
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            
            # 인증된 사용자 여부 확인
            if user is not None:
                login(request, user)  # 로그인 처리
                return redirect("common:profile")
            else:
                messages.error(request, "아이디 또는 비밀번호가 일치하지 않습니다.")
        else:
            # 폼 검증 에러 처리
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
            
            return render(request, "common/login.html", {"form": form})
    
    # GET 요청 시 빈 폼을 반환
    form = LoginForm()
    return render(request, "common/login.html", {"form": form})

def common_logout(request):
    logout(request)
    return render(request,"common/login.html")


def common_find_username(request):
    if request.method == "POST":
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            try:
                # get으로 사용자 검색
                user = User.objects.filter(
                    first_name=form.cleaned_data["first_name"],
                    email=form.cleaned_data["email"],
                ).first()
                return render(request, "common/find_username.html", {"username": user.username})
            except User.DoesNotExist:
                # 조건에 맞는 사용자가 없을 때 메시지 출력
                messages.error(request, "일치하는 사용자를 찾을 수 없습니다.")
        else:
            # 폼 유효성 검사 실패 시 오류 메시지 출력
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
    
    # GET 요청 또는 처리 실패 시 빈 폼 렌더링
    form = FindUsernameForm()
    return render(request, "common/find_username.html", {"form": form})



def generate_password():
    import random
    import string
    length = random.randint(8,20)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def common_reset_password(request):
    if request.method =="POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(
                first_name = form.cleaned_data["first_name"],
                email = form.cleaned_data["email"],
                username = form.cleaned_data["username"]
            ).first()
            
            if user is not None:
                password = generate_password()
                user.set_password(password)
                user.save()
                return render(request, "common/reset_password.html",{"password": password})
            else:
                messages.error(request,"존재하지 않는 사용자입니다.")
        else:
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
            
    form = FindUsernameForm()
    return render(request,"common/reset_password.html")

def common_profile(request):
    return render(request,"common/profile.html")

def common_update_profile(request):
    return render(request,"common/update_profile.html")

def common_update_password(request):
    return render(request,"common/update_password.html")
