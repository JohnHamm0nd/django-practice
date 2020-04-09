from django import forms
from .models import Post
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'width: 100%; height: 100%', 'placeholder': '내용을 입력하세요.'}
            ),
        }

        labels = {
            'title': '제목',
            'text': '내용'
        }

