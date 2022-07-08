from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # print(request.headers)
    return render(request, 'base.html')


def posts(request, post_id):
    #print(post_id)
    # post_content = request.headers
    # return render(request, 'posts.html', {'content': post_content})
    # if request.method == "GET":
    #     print((request.GET))
    return render(request, 'posts.html', {'content': request.GET})


def about(request):
    return render(request, 'about.html', {'content': '<h1>About</h1>'})


def info(request):
    return render(request, 'about.html', {'content': '<h1>_I_N_F_O_</h1>'})
