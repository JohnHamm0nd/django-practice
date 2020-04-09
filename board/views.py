from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect, render  # 오브젝트가 없으면 404에러를 띄어준다
from django.contrib.auth.mixins import LoginRequiredMixin  # 로그인한 사용자만 사용할수 있게 하는 모듈

# Create your views here.
# 클래스뷰 사용

class PostListView(ListView):
    """
	ListView 디폴트 지정 속성
	1) 컨텍스트 변수 : object_list
	2) 템플릿 파일 : bookmark_list.html (모델명소문자_list.html)
	"""
    model = Post
    paginate_by = 10  # 페이지네이션(10개씩 가져온다)
    ordering = ['-id']  # 모델에서 정렬시키지 않고 view에서 정렬 시키는 방법


class PostDetailView(DetailView):
    """
	DetailView 디폴트 지정 속성
	1) 컨텍스트 변수 : object (URLConf 에서 pk 파라미터 값을 활용하여 DB 레코드 조회)
	2) 템플릿 파일 : bookmark_detail.html (모델명소문자_detail.html)
	"""
    model = Post

    # get_ojbect를 변경, url에서 넘어온 인자로 데이터를 찾아 count를 1 더해준다. 데이터가 없어도 save()함수에서 문제는 발생하지 않는다(왜?), 똑같이 404 에러를 띄워준다.
    def get_object(self):
        id_ = self.kwargs.get('pk')
        obj = get_object_or_404(Post, id=id_)
        obj.count += 1
        obj.save()
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "board/post_form.html"
    success_url = '/board'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(PostCreateView, self).form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "board/post_update.html"
    success_url = '/board'
    
    # 글을 작성한 유저와 수정하려는 유저가 같은지 체크하는 쉬운 방법
    # 원칙적? 으로 체크를 하려면 request.user 와 수정하려는 object의 user (여기에서는 author) 가 같은지 체크를 한 후 같으면 수정폼을, 같지 않으면 접근금지를 주어야 한다.
    # 이 방법은 데이터모델에 쿼리를 보낼 때 쿼리셋에 필터를 추가하여 (기본 글의 id + author로 request.user) 데이터 모델에서 글을 찾을 때 글번호 + 수정요청을 보낸 user 로 찾게 하여
    # 해당 글의 author가 수정요청을 보낸 user와 다를 경우 검색 결과가 없게 만들어 404 에러를 띄우게 만든다.
    # 원칙적? 으로 막는 방법은 더 어렵고 복잡해 보인다. 현재는 구현하기 어려우므로 추 후 구현하도록 하자.
    
    def get_queryset(self):
       queryset = super(PostUpdateView, self).get_queryset()
       queryset = queryset.filter(author=self.request.user)
       return queryset

    #def get_object(self): 
    #    Post = get_object_or_404(Post, pk=self.kwargs['pk']) #4
    #    return Post


""" 회원가입 방식으로 변경
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/board'
    
    def delete(self, request, *args, **kwargs):
        '''
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        '''
        self.object = self.get_object()
        success_url = self.get_success_url()
        if request.POST['password'] == self.object.password:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponse('비밀번호가 틀립니다.')

"""


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/board'
    
    def get_queryset(self):
        queryset = super(PostDeleteView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
