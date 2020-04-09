from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'board'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),  # board 앱에서 뒤에 아무 주소 입력이 없을 때 views에 PostListView 호출.
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]
