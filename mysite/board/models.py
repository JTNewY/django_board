from django.db import models


class Board(models.Model):
    title = models.CharField(verbose_name="제목",max_length=100 )
    content = models.TextField(verbose_name="내용")
    password = models.CharField(verbose_name="비밀번호",max_length=20 )
    created_by = models.CharField(verbose_name="작성자",max_length=20)
    created_at = models.DateTimeField(verbose_name="작성일시",auto_now_add=True)
    
    class Meta:
        db_table = 'board'
        verbose_name = 'board'
        verbose_name_plural = 'boards'
        ordering = ['-created_at']
        

    def __str__(self):
        return self.title