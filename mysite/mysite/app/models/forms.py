from django import forms
from mysite.app.models.models import Question

class add_question_form(forms.Form):
    otvet_tittle = forms.CharField(label="Enter tittle", max_length=30)
    otvet_text = forms.CharField(label="Enter your question", max_length=255)
class add_answer(forms.Form):
    text = forms.CharField(label="Введите ответ", max_length=255)
class form_invite(forms.Form):
    login = forms.CharField(label="Login", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=16)
class form_reg(forms.Form):
    login = forms.CharField(label="Login", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=16)