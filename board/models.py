from django.db import models
from django.utils import timezone  # 글 작성 시간 저장을 위해 시간 관련 라이브러리 임포트
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=10, blank = True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    pub_date = models.DateTimeField(default = timezone.now)
    count = models.IntegerField(default = 0)
    
    """
    # 가장 최근 글이 가장 위로 올라오게 하는 방법으로 모델에서 정렬 순서를 지정 할 수 있다.
    class Meta:
        ordering = ['-id']
    """
