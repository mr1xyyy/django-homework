from django.shortcuts import render, redirect
from .models import News
from .forms import ArticleForm 

def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Maqola noto'g'ri edi"

    form = ArticleForm()

    data = {
        'form' : form,
        'error': error
    }

    return render(request, 'news/create.html', data)