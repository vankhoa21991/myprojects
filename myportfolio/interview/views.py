from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from random import randint
import random

from .models import Question
from .forms import QuestionForm
# Create your views here.

@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'interview/interview_index.html')

@login_required
def testQuestion(request):
    if request.method == 'POST':
        job = request.POST.get('job')
        na = request.POST.get('nationality')

        if job:
            questions = Question.objects.filter(option=True)
        elif na:
            questions = Question.objects.filter(option=False)
        else:
            questions = Question.objects.all()
        ID = [question.id for question in questions]
        rand_entities = randint(0, len(ID)-1)

        questions = Question.objects.filter(id=ID[rand_entities])
        return render(request,'interview/interview_test.html', {'questions': questions})
    else:
        return render(request,'interview/interview_index.html')

@login_required
def nextQuestion(request,question_id):
    questions = Question.objects.filter(id=question_id)
    option = [question.option for question in questions]
    print(type(option))
    if request.method == 'GET':
        questions = Question.objects.filter(option=option[0])
        ID = [question.id for question in questions]
        rand_entities = randint(0, len(ID)-1)

        questions = Question.objects.filter(id=ID[rand_entities])
        return render(request,'interview/interview_test.html', {'questions': questions})
    else:
        questions = Question.objects.filter(option=option)
        ID = [question.id for question in questions]
        rand_entities = randint(0, len(ID)-1)

        questions = Question.objects.filter(id=ID[rand_entities])
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        return render(request,'interview/interview_next.html', {'questions': questions})


@login_required
def addQuestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():

            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            option= form.cleaned_data['option']


            newquestion = Question(question = str(question),answer = str(answer),option = option)

            newquestion.save()
            questions = Question.objects.all()
            return render(request,'interview/interview_all.html', {'questions': questions})
    else:
        form = QuestionForm()
    return render(request,'interview/interview_add.html', {'form': form})

@login_required
def allQuestion(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        return render(request,'interview/interview_all.html', {'questions': questions})


@login_required
def deleteQuestion(request,question_id):
    questionToDelete = Question.objects.filter(id=question_id)
    print(questionToDelete)
    if request.method == 'POST':
        questionToDelete = Question.objects.filter(id=question_id).delete()
        questions = Question.objects.all()
        return render(request,'interview/interview_all.html', {'questions': questions})
    else:
        return render(request,'interview/interview_delete.html',{'questions': questionToDelete})


@login_required
def editQuestion(request,question_id):
    questionToEdit = Question.objects.filter(id=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():


            newquestion = form.cleaned_data['question']
            newanswer = form.cleaned_data['answer']
            newoption= form.cleaned_data['option']

            Question.objects.filter(id=question_id).update(question = str(newquestion))
            Question.objects.filter(id=question_id).update(answer = str(newanswer))
            Question.objects.filter(id=question_id).update(option = str(newoption))

            questions = Question.objects.all()
            return render(request,'interview/interview_all.html', {'questions': questions})
    else:
        form = QuestionForm()
    return render(request,'interview/interview_edit.html', {'form': form, 'questions': questionToEdit})
