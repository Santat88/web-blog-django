
from django.urls import path
from .views import feedback_page, add_feedback_page, thanks_page

urlpatterns = [
    path('', feedback_page, name = 'feedback_list'),
    path('add_feedback/', add_feedback_page, name = 'add_feedback_record'),
    path('thanks/', thanks_page)
]
