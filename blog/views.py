from django.shortcuts import render

posts = [
    {
        'author': 'Farrakhan',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date_posted': 'August 2, 2019'
    },
    {
        'author': 'Farrakhan',
        'title': 'Post 2',
        'content': 'Post 2 content',
        'date_posted': 'August 3, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
