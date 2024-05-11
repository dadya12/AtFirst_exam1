from django.db import models

status_field = [("active", "Активно"), ("blocked", "Заблокировано")]


class GuestBook(models.Model):
    author_name = models.CharField(max_length=50, verbose_name='Имя автора')
    author_gmail = models.EmailField(verbose_name='Почта автора', max_length=200)
    text = models.TextField(max_length=100, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(verbose_name='Статус', default='active', choices=status_field, max_length=50)

    def __str__(self):
        return f'{self.author_name} {self.status}'
