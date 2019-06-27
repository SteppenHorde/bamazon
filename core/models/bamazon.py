from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



# Автор является полностью отдельной от auth.User сущностью (не предполагается,
# что автор может быть пользователем сайта и иметь особый доступ к своему профилю,
# книгам и т.д.). Т.е. менять его профиль, книги может только команда магазина.
# Соответственно - все поля только для репрезентации
# Данная реализация кажется мне обоснованной
class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество (если есть)', max_length=50, blank=True, null=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения')
    death_date = models.DateTimeField(verbose_name='Дата смерти', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='images/authors', blank=True, null=True)
    bio = models.TextField(verbose_name='Биография')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(verbose_name='Название', max_length=100)
    desc = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2) # max = 999999.99
    pub_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def was_published_recently(self): # для сортировки по дате
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Опубликовано недавно?'

    def get_absolute_url(self):
        book_id = self.id
        return reverse('show_book', kwargs={
                                            'book_id': book_id,
                                    })
