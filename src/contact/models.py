from django.db import models


class Contact(models.Model):
    """Таблица Контакты"""
    name = models.CharField('Имя', max_length=30)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Номер телефона', max_length=50)
    subject = models.CharField('Тема', max_length=50)
    message = models.TextField('Текст сообщения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
