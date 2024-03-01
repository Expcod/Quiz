
from django.urls import path
from . import views

urlpatterns = [
    path('api/quiz/<str:code>/', views.get_quiz_detail),
]
