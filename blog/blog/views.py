from django.shortcuts import render

MENU = {'Главная':'/','Страница поста':'/post','О блоге':'/about'}

def main_page(request):
    title = 'Главная страница'
    data = {"menu":MENU,"title":title}
    return render(request, './index.html', context=data)

def post_page(request):
    title = 'Страница поста'
    data = {"menu":MENU,"title":title}
    return render(request, './post.html', context=data)

def about_page(request):
    title = 'Cтраница о блоге'
    data = {"menu":MENU,"title":title}
    return render(request, './about.html', context=data)