from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts  = Post.objects.order_by('-pubished')
    return render(request, 'posts/index.html', {'posts': posts})
    
    # return HttpResponse("Hello World! このページは投稿のインデックスです。") 


# Create your views here.
