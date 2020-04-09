from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')  # index함수 호출시 home 앱의 index.html을 렌더링하여 보낸다. 
