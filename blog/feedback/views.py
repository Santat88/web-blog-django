from django.shortcuts import render

MENU = {'Главная':'/','Страница поста':'/post','О блоге':'/about', 'Отзывы':'/feedback'}

def feedback_page(request):
    title = 'Cтраница с отзывами'
    data = {"menu":MENU,"title":title}
    return render(request, './feedback.html', context=data)
