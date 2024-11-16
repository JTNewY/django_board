from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BoardForm
from board.models import Board

# 등록
def board_create(request):
    # 입력폼 (비어있는 값)
    form = BoardForm()
    
    # 처리
    if request.method == "POST":
        # 사용자가 입력한 데이터를 폼에 저장
        form = BoardForm(request.POST)
        
        # 입력 폼 유효성 검사
        if form.is_valid():  # 통과가 되었다면 진행 
            # 검사 성공
            board = form.save(commit=False)  # 들어온 정보를 준비만 해라
            board.save()  # DB에 저장
            return HttpResponse("게시글 등록 성공")
        else: 
            # 검사 실패
            # 에러메시지 띄우기
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
        
    return render(request, "board/create.html" )

# 상세보기
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {"board": board}
    return render(request, "board/detail.html", context)
# 수정

# 삭제

