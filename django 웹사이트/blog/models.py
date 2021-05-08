from django.db import models

class Post(models.Model):   # Post Model 만들기
    title = models.CharField(max_length=30) #제목
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
