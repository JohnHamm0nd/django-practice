from django.contrib import admin
from .models import VisualLocalization

# Register your models here.
# admin 페이지에서 모델을 커스터마이징 하기 위해(기본 admin 페이지에서는 id값이 안보인다) ModelAdmin 상속.
class VisualLocalizationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  # id 필드를 추가

admin.site.register(VisualLocalization, VisualLocalizationAdmin)  # admin 페이지에서 VisualLocalization 데이터베이스를 사용하기 위해 등록, 참고: admin클래스를 먼저 쓰면 안된다.

