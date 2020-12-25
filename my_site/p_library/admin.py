from django.contrib import admin

from p_library.models import Author, Book, Friend, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'ISBN', 'year_release', 'author', 'copy_count', 'price', 'publisher', 'friend')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email')