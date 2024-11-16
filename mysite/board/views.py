from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BoardForm,BoardDeleteForm
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
            messages.success(request,"게시글을 등록되었습니다.")
            return redirect("board:read", board_id=board.id)
        else: 
            # 검사 실패
            # 에러메시지 띄우기
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
        
    return render(request, "board/create.html" )

# 상세보기
def board_read(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {"board": board}
    return render(request, "board/read.html", context)

# 수정
def board_update(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {"board": board}

    if request.method == "POST":
        
        form = BoardForm(request.POST)
        if form.is_valid():
            old_password = board.password
            new_password = form.cleaned_data.get("password")
            
            if old_password == new_password:
                # 게시글 수정
                board = form.save(commit=False)
                board.save()
                
                messages.success(request,"게시글을 수정하였습니다.")
                return redirect("board:read", board_id=board.id)
            else:
                messages.error(request, "비밀번호가 일치하지 않습니다.")
    #검사실패
        else:
            for field_name, error_message in form.errors.items():
                messages.error(request, f"{form.fields[field_name].label}: {error_message[0]}")
        
    # GET 요청일때 빈 폼 반환
    form = BoardForm(instance=board)
    # board의 값을 instance에 넘긴다.
    # 화면으로 넘김
    context["form"] = form
    
    # 화면
    return render(request, "board/update.html", context)

# 삭제
def board_delete (request, board_id):
    board = Board.objects.get(id=board_id)
    
    if request.method == "POST":
        form = BoardDeleteForm(request.POST)
        
        if form.is_valid():
            old_password = board.password
            new_password = form.cleaned_data.get("password")
            
            if old_password == new_password:
                board.delete()
                return HttpResponse("게시글이 삭제되었습니다.")
            else:
                messages.error(request,"비밀번호가 일치하지 않습니다")
                return redirect("board:read", board_id=board.id)       


# 목록
def board_list(request):
    boards = Board.objects.all()
    context = {"boards":boards}
    return render(request, "board/list.html", context)    