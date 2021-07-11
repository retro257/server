from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main_page, name="main_page"),
    url(r'^question/(?P<question_number>\d+)', views.question, name="question"),
    path("add_question", views.add_question, name="add_question"),
    path("invite/", views.invite, name="invite"),
    path("reg/", views.reg, name="reg")
]
