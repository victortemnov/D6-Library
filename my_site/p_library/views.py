from p_library.forms import AuthorForm
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from p_library.models import Author, Book, Friend, Publisher


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    lib_data = {
        'title': 'Welcome to my personal library',
        'books': books,
    }
    return HttpResponse(template.render(lib_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if  request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def publishers_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    pub_data = {
        'title': 'Publishers',
        'publishers': publishers,
    }
    return HttpResponse(template.render(pub_data))


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_read')
    template_name = 'author_create.html'


class AuthorRead(ListView):
    model = Author
    template_name = 'author_read.html'


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_read')
    template_name = 'author_update.html'


class AuthorDelete(DeleteView):
    model = Author
    form_class = AuthorForm
    fields = ('full_name', 'birth_year', 'country')
    success_url = reverse_lazy('p_library:author_read')
    template_name = 'author_delete.html'


def friends_list(request):
    template = loader.get_template('friends.html')
    friends = Friend.objects.all()
    friends_data = {
        'friends': friends,
    }
    return HttpResponse(template.render(friends_data, request))