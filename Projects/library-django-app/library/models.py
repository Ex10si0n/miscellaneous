from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
import uuid


def is_cn(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        if is_cn(self.first_name):
            return '%s%s' % (self.last_name, self.first_name)
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('author')


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    summary = models.CharField(max_length=500)
    ISBN = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    def get_absolute_url(self):
        return reverse('book_desc', args=[str(self.id)])


class BookCopies(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Id for this book across whole library')
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability', 
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    def get_absolute_url(self):
        return reverse('copies_list')

