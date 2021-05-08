from django.db import models
import os

class Post(models.Model):   # Post Model 만들기
    title = models.CharField(max_length=30) #제목
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()            #내용
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)      #작성일
    updated_at = models.DateTimeField(auto_now=True)         #수정일
    #author
    
    def __str__(self):
        return f'[{self.pk}]{self.title}' #self.pk는 포스트 번호, self.title은 포스트 제목

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self): #확장자 찾아내는 함수
        return self.get_file_name().split('.')[-1]
