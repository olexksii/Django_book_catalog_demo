from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

import numpy
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    x = numpy.median(speed)

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instance_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'x': x,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book

# Create your views here.
