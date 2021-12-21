from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Question(models.Model):
    TEXT = 'TEXT'
    CHOICE = 'CHOICE'
    MULTICHOICE = 'MULTICHOICE'
    QUESTION_TYPES = [
        (TEXT, 'TEXT'),
        (CHOICE, 'CHOICE'),
        (MULTICHOICE, 'MULTICHOICE')
    ]
    text = models.TextField(verbose_name='Содержание вопроса')
    type = models.CharField(max_length=12, choices=QUESTION_TYPES, default=TEXT)

    def __str__(self):
        return self.text


class Survey(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название опроса')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание опроса')
    questions = models.ManyToManyField(Question, related_name='questions')

    def __str__(self):
        return self.title


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    text = models.CharField(max_length=127)
    user = models.IntegerField()

    def __str__(self):
        return f'Ответ {self.text} на вопрос {self.question}'
