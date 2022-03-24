"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя',min_length=2,max_length=100)
    city = forms.CharField(label='Ваш род занятий',min_length=2,max_length=100)
    role = forms.CharField(label='Что будет представлять из себя ваш сайт?',min_length=2,max_length=400)
    computer = forms.ChoiceField(label='Под какую ОС был написан ваш сайт?',
                                 choices=(('1','Linux'),
                                          ('2','Windows')),initial=1)
    adverst = forms.ChoiceField(label='Хотели бы вы видить рекламу на вашем сайте?',
                                choices=[('1','Да'),('2','Нет')], widget=forms.RadioSelect,initial=1)
    notice = forms.BooleanField(label='Получать уведомления о скидках на e-mail?',required = False)
    email = forms.EmailField(label='Ваш e-mail',min_length=7)
    message = forms.CharField(label='Что вы хотели бы улучшить в нашем сервисе',widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':'Комментарий'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {"title","description","content","image",}
        labels = {"title":"Заголовок","description": "Краткое содержание","content":"Полное содержание","image":"Картинка"}
    
