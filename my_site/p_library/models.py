from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Friend(models.Model):
    full_name = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True, related_name='publishers')
    friend = models.ForeignKey(Friend, on_delete=models.SET_NULL, null=True, blank=True, related_name='friends')
    book_img = models.ImageField(blank=True, null=True, upload_to='books_img')

    def __str__(self):
        return self.title
