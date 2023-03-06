from django.contrib.sites import requests
from django.db import models
from django.shortcuts import render
from django.template.context_processors import media


from django.db.models import QuerySet

class Ivan_Mazur(models.Model):
    задание = models.ForeignKey(
        'core.Задания',
        on_delete = models.deletion.SET_NULL,
        related_name='задание',
        null = True,
        blank = False
    )
    @property
    def задания_history(self):
        return self.Ivan_Mazur_задание_history.all()

class Dima_Vinokurov(models.Model):
    task = models.ForeignKey(
        'core.Задания',
        on_delete = models.deletion.SET_NULL,
        related_name='task',
        null = True,
        blank = False
    )
    @property
    def задания_history(self):
        return self.Dima_Vinokurov_task_history.all()

class Katya_Sidorina(models.Model):
    work = models.ForeignKey(
        'core.Задания',
        on_delete = models.deletion.SET_NULL,
        related_name='work',
        null = True,
        blank = False
    )
    @property
    def задания_history(self):
        return self.Katya_Sidorina_work_history.all()


class Задания (models.Model):
    создал = models.CharField(
        max_length=255, null=False, blank=True
    )
    содержание = models.CharField(
        max_length=1000, null=False, blank=True
    )
    отвественный = models.CharField(
        max_length=255, null=False, blank=True
    )
    дата_создания = models.CharField(
        max_length=255, null=False, blank=True
    )
    дата_выполения = models.CharField(
        max_length=255, null=False, blank=True
    )
    срок = models.CharField(
        max_length=255, null=False, blank=True
    )
    отчет = models.CharField(
        max_length=255, null=False, blank=True
    )
    файл_задания = models.FileField()

    файл_задания_резерв = models.FileField(
        max_length=255, null=False, blank=True,
    )
    файл_выполнения = models.FileField(
        max_length=255, null=False, blank=True,
    )
    файл_выполнения_резерв = models.FileField(
        max_length=255, null=False, blank=True,
    )
    статус = models.CharField(
        max_length=255, null=False, blank=True
    )
    дата_последних_изменений = models.CharField(
        max_length=255, null=False, blank=True
    )

