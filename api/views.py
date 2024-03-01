
from django.http import JsonResponse
from main.models import *

def get_quiz_detail(request, code):
    try:
        quiz = Quiz.objects.get(code=code)
        questions = Question.objects.filter(quiz=quiz)
        quiz_data = {
            'id': quiz.id,
            'title': quiz.title,
            'description': quiz.description,
            'questions': [{'id': q.id, 'text': q.text} for q in questions]
        }
        return JsonResponse({'quiz': quiz_data})
    except Quiz.DoesNotExist:
        return JsonResponse({'error': 'Quiz not found'}, status=404)

