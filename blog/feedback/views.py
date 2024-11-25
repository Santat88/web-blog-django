from django.shortcuts import render
from .models import feedbackRecord

MENU = {'Главная':'/','Страница поста':'/post','О блоге':'/about', 'Отзывы':'/feedback'}

def feedback_page(request):
    feedbackRecords = feedbackRecord.objects.all()
    title = 'Cтраница с отзывами'
    data = {"menu":MENU,"title":title,"feedbackRecords":feedbackRecords}
    return render(request, './feedback.html', context=data)
    
    
def add_feedback_page(request):
    title = 'Добавить отзыв'
    data = {"menu":MENU,"title":title}
    return render(request, './add_feedback.html', context=data)
    
def thanks_page(request):
    Name = request.POST['name']
    Email = request.POST['email']
    Text = request.POST['text']
    feedbackRecord.objects.create(name = Name, email = Email, text = Text)
    title = 'Спасибо за Ваш отзыв!'
    data = {"menu":MENU,"title":title}
    return render(request, './thanks.html', context=data)
