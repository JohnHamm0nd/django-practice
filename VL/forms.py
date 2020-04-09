from django import forms
from .models import VisualLocalization


class PhotoForm(forms.ModelForm):
    class Meta:
        model = VisualLocalization
        fields = ['photo']  # VisualLocalization모델의 photo 속성만 사용한다는 뜻이다, 원하는 필드만 폼에 넣을 수 있다.

class TrueCountryForm(forms.ModelForm):
    class Meta:
        model = VisualLocalization
        fields = ['true_country']
