from django.shortcuts import render
from vote.models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    question_dict = {'question_list': question_list}
    return render(request, 'index.html', question_dict)