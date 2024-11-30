from django.urls import path
from . import views

# 사용자 가입 /common/register 
# 사용자 아이디 찾기 /common/find_username
# 사용자 비밀번호 초기화 /common/reset_password
# 사용자 로그인 /common/login
# 사용자 로그아웃 /common/logout
# 사용자 정보 /common/profile
# 사용자 정보 수정 /common/update_profile
# 사용자 비밀번호 수정 /common/update_password/

app_name = "common"

urlpatterns = [
    path("register/", views.common_register, name="register"),  # 사용자 가입
    path("find_username/", views.common_find_username, name="find_username"),  # 사용자 아이디 찾기
    path("reset_password/", views.common_reset_password, name="reset_password"),  # 사용자 비밀번호 초기화
    path("login/", views.common_login, name="login"),  # 사용자 로그인
    path("logout/", views.common_logout, name="logout"),  # 사용자 로그아웃
    path("profile/", views.common_profile, name="profile"),  # 사용자 정보
    path("update_profile/", views.common_update_profile, name="update_profile"),  # 사용자 정보 수정
    path("update_password/", views.common_update_password, name="update_password"),  # 사용자 비밀번호 수정
]