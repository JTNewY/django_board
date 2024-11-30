from django import forms
from .models import Board
from tinymce.widgets import TinyMCE


# 등록 폼
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "content", "password", "created_by"]
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("제목을 입력하세요.")
        if len(title) < 2 or len(title) > 100:
            raise forms.ValidationError("제목을 2자이상 100자이하로 입력하세요.")
        return title
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("내용을 입력하세요.")
        return content
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("비밀번호를 입력하세요.")
        if len(password) < 2 or len(password) > 20:
            raise forms.ValidationError("비밀번호를 2자이상 20자이하로 입력하세요.")
        return password
    
    def clean_created_by(self):
        created_by = self.cleaned_data.get("created_by")
        if not created_by:
            raise forms.ValidationError("글쓴이 이름을 입력하세요.")
        if len(created_by) < 2 or len(created_by) > 20:
            raise forms.ValidationError("글쓴이 이름을 2자이상 20자이하로 입력하세요.")
        return created_by
    
# 삭제 폼
# 삭제할때는 비밀번호만 넘겨야되니까 만들었다.
class BoardDeleteForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [ "password"]
        
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("비밀번호를 입력하세요.")
        return password
