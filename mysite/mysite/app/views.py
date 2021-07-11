from django import forms, http
import django
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.app.models.models import Answer, Question
from mysite.app.models.forms import add_question_form, add_answer, form_invite, form_reg
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from django.utils.crypto import get_random_string

from django.contrib.auth import authenticate, login

def main_page(requests):
    for i in Question.objects.all():
        print(i.tittle)
    questions = Question.objects.order_by("-id")
    return HttpResponse(render(requests, "main.html", {"questions":questions, "requests":requests}))
def question(requests, question_number):
    if not requests.user.is_authenticated:
        return HttpResponseRedirect("http://127.0.0.1:8000/reg")
    number = question_number
    question = Question.objects.get(pk=number)
    answers = Answer.objects.filter(question=question)
    if requests.method == "GET":
        form = add_answer()
    else:
        form = add_answer(requests.POST)
        if form.is_valid():
            answer = Answer.objects.create(author=requests.user, text=form.cleaned_data["text"], question=question)
            
            HttpResponseRedirect("http://127.0.0.1:8000/question/"+str(question_number))
    return HttpResponse(render(requests, "question.html", {"question":question, "answers":answers, "form":form, "number":question_number, "requests":requests}))
def add_question(requests):
    if not requests.user.is_authenticated:
        return HttpResponseRedirect("http://127.0.0.1:8000/reg")
    if requests.method == "GET":
        form = add_question_form()
    else:
        form = add_question_form(requests.POST)
        if form.is_valid():
            question = Question(tittle=form.cleaned_data["otvet_tittle"], content_text=form.cleaned_data["otvet_text"]) 
            question.save() 
            return HttpResponseRedirect("http://127.0.0.1:8000/main")
    return HttpResponse(render(requests, "add_quest.html", {"form":form, "requests":requests}))
def invite(requests):
    if requests.method == "GET":
        form = form_invite()
    else:
        form = form_invite(requests.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data["login"])
                if user.email == form.cleaned_data["password"]:
                    login(requests,user)
                    requests.session['sessionid'] = get_random_string(32)
                    requests.session['password'] = user.password
                    print(requests.user)
                    return HttpResponseRedirect("http://127.0.0.1:8000/main")
                else:
                    return(HttpResponse(render(requests, "invite.html", {"form":form})))
            except BaseException:
                return HttpResponse("Такого логина нет")
                
    return(HttpResponse(render(requests, "invite.html", {"form":form, "requests":requests})))

def reg(requests):
    if requests.method == "GET":
        form = form_reg()
    else:
        form = form_reg(requests.POST)
        if form.is_valid():
            try:
                new_user = User.objects.create_user(password=form.cleaned_data["password"], username=form.cleaned_data["login"], email=form.cleaned_data["password"])
                new_user.save()
                user = authenticate(username=form.cleaned_data["login"], password=form.cleaned_data["password"]) 
                if user is not None:
                    login(requests,user)
                print(requests.user)
                requests.session['sessionid'] = get_random_string(32)
                requests.session['password'] = form.cleaned_data["password"]
                return HttpResponseRedirect("http://127.0.0.1:8000/main")
            except ValueError:
                return HttpResponse("Пользователь с таким логином существует")
    return HttpResponse(render(requests, "reg.html", {"form":form, "requests":requests}))
#(?P<name>\w+)