from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book, Order, PublishingHouse

# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'nationality', 'number_of_publications', 'genre']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'nationality', 'number_of_publications', 'genre']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    fields = ['publishing_house', 'name', 'author', 'genre', 'publication_date', 'language', 'price', 'availability']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['publishing_house', 'name', 'author', 'genre', 'publication_date', 'language', 'price', 'availability']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    fields = ['customer_name', 'order_date', 'order_status', 'total_amount']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer_name', 'order_date', 'order_status', 'total_amount']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')


# PublishingHouse Views
class PublishingHouseListView(ListView):
    model = PublishingHouse
    template_name = 'publishinghouse_list.html'
    context_object_name = 'publishinghouses'


class PublishingHouseDetailView(DetailView):
    model = PublishingHouse
    template_name = 'publishinghouse_detail.html'
    context_object_name = 'publishinghouse'


class PublishingHouseCreateView(CreateView):
    model = PublishingHouse
    fields = ['name', 'location', 'year_of_fundation', 'telephone_number', 'website']
    template_name = 'publishinghouse_form.html'
    success_url = reverse_lazy('publishinghouse_list')


class PublishingHouseUpdateView(UpdateView):
    model = PublishingHouse
    fields = ['name', 'location', 'year_of_fundation', 'telephone_number', 'website']
    template_name = 'publishinghouse_form.html'
    success_url = reverse_lazy('publishinghouse_list')


class PublishingHouseDeleteView(DeleteView):
    model = PublishingHouse
    template_name = 'publishinghouse_confirm_delete.html'
    success_url = reverse_lazy('publishinghouse_list')
