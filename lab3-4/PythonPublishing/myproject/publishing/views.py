from unicodedata import category

from bokeh.embed import components
from bokeh.plotting import graph
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Author, Book, Order, PublishingHouse

# Author Views
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST.get('date_of_birth', None)
        nationality = request.POST.get('nationality', None)
        number_of_publications = request.POST['number_of_publications']
        genre = request.POST.get('genre', None)
        Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            nationality=nationality,
            number_of_publications=number_of_publications,
            genre=genre
        )
        return redirect('author_list')
    return render(request, 'author_form.html')

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.date_of_birth = request.POST.get('date_of_birth', None)
        author.nationality = request.POST.get('nationality', None)
        author.number_of_publications = request.POST['number_of_publications']
        author.genre = request.POST.get('genre', None)
        author.save()
        return redirect('author_list')
    return render(request, 'author_form.html', {'author': author})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'author': author})


# Book Views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    publishing_house = PublishingHouse.objects.all()
    authors = Author.objects.all()
    if request.method == 'POST':
        publishing_house_id = request.POST['publishing_house']
        name = request.POST['name']
        author_id = request.POST.get('author', None)
        genre = request.POST['genre']
        publication_date = request.POST['publication_date']
        language = request.POST['language']
        price = request.POST['price']
        availability = request.POST['availability']
        Book.objects.create(
            publishing_house_id=publishing_house_id,
            name=name,
            author_id=author_id,
            genre=genre,
            publication_date=publication_date,
            language=language,
            price=price,
            availability=availability
        )
        return redirect('book_list')
    return render(request, 'book_form.html', {'publishinghouses': publishing_house, 'authors': authors})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.publishing_house_id = request.POST['publishing_house']
        book.name = request.POST['name']
        book.author_id = request.POST.get('author', None)
        book.genre = request.POST['genre']
        book.publication_date = request.POST['publication_date']
        book.language = request.POST['language']
        book.price = request.POST['price']
        book.availability = request.POST['availability']
        book.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        order_date = request.POST['order_date']
        order_status = request.POST['order_status']
        total_amount = request.POST.get('total_amount', None)
        Order.objects.create(
            customer_name=customer_name,
            order_date=order_date,
            order_status=order_status,
            total_amount=total_amount
        )
        return redirect('order_list')
    return render(request, 'order_form.html')

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.customer_name = request.POST['customer_name']
        order.order_date = request.POST['order_date']
        order.order_status = request.POST['order_status']
        order.total_amount = request.POST.get('total_amount', None)
        order.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'order': order})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})


# PublishingHouse Views
def publishinghouse_list(request):
    publishinghouses = PublishingHouse.objects.all()
    return render(request, 'publishinghouse_list.html', {'publishinghouses': publishinghouses})

def publishinghouse_detail(request, pk):
    publishinghouse = get_object_or_404(PublishingHouse, pk=pk)
    return render(request, 'publishinghouse_detail.html', {'publishinghouse': publishinghouse})

def publishinghouse_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        year_of_fundation = request.POST['year_of_fundation']
        telephone_number = request.POST['telephone_number']
        website = request.POST.get('website', None)
        PublishingHouse.objects.create(
            name=name,
            location=location,
            year_of_fundation=year_of_fundation,
            telephone_number=telephone_number,
            website=website
        )
        return redirect('publishinghouse_list')
    return render(request, 'publishinghouse_form.html')

def publishinghouse_update(request, pk):
    publishinghouse = get_object_or_404(PublishingHouse, pk=pk)
    if request.method == 'POST':
        publishinghouse.name = request.POST['name']
        publishinghouse.location = request.POST['location']
        publishinghouse.year_of_fundation = request.POST['year_of_fundation']
        publishinghouse.telephone_number = request.POST['telephone_number']
        publishinghouse.website = request.POST.get('website', None)
        publishinghouse.save()
        return redirect('publishinghouse_list')
    return render(request, 'publishinghouse_form.html', {'publishinghouse': publishinghouse})

def publishinghouse_delete(request, pk):
    publishinghouse = get_object_or_404(PublishingHouse, pk=pk)
    if request.method == 'POST':
        publishinghouse.delete()
        return redirect('publishinghouse_list')
    return render(request, 'publishinghouse_confirm_delete.html', {'publishinghouse': publishinghouse})

from rest_framework import generics
from .models import PublishingHouse, Author, Order, Book
from .serializers import PublishingSerializer, AuthorSerializer, OrderSerializer, BookSerializer

# PublishingHouse Views
class PublishingHouseListCreateView(generics.ListCreateAPIView):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingSerializer


class PublishingHouseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingSerializer


# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorRegistrationSerializer

class AuthorRegistrationView(APIView):
    def post(self, request):
        serializer = AuthorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorLoginSerializer

class AuthorLoginView(APIView):
    def post(self, request):
        serializer = AuthorLoginSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.validated_data
            return Response({
                "message": "Login successful",
                "author_id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author

# Реєстрація
def register_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST.get('date_of_birth')
        nationality = request.POST.get('nationality')
        number_of_publications = request.POST['number_of_publications']
        genre = request.POST.get('genre')

        # Створення автора
        author = Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            nationality=nationality,
            number_of_publications=number_of_publications,
            genre=genre
        )
        messages.success(request, 'Registration successful!')
        return redirect('login_author')

    return render(request, 'register.html')

# Логін
def login_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            author = Author.objects.get(first_name=first_name, last_name=last_name)
            messages.success(request, 'Login successful!')
            return redirect('publishinghouse_list')  # Перенаправлення на головну сторінку автора
        except Author.DoesNotExist:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'login.html')


import plotly.express as px
from django.shortcuts import render
from .models import Author


def author_publications_graph(request):
    # Отримуємо дані з моделі Author
    authors = Author.objects.all()
    data = {
        'Author': [f'{author.first_name} {author.last_name}' for author in authors],
        'Number of Publications': [author.number_of_publications for author in authors]
    }

    # Створюємо графік з використанням Plotly
    fig = px.bar(data, x='Author', y='Number of Publications', title="Number of Publications by Author")

    # Генеруємо HTML-код для вбудовування графіка
    graph_html = fig.to_html(full_html=False)

    # Повертаємо графік в шаблон
    return render(request, 'author_publications_graph.html', {'graph_html': graph_html})

from django.shortcuts import render
import plotly.express as px
from .models import Book
import pandas as pd

from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from .models import Book  # Ваші моделі
from django.db.models import Sum

def income_by_genre(request):
    # Отримуємо агреговані дані за жанрами (наприклад, сумарний дохід по кожному жанру)
    genres_income = Book.objects.values('genre').annotate(total_income=Sum('price')).order_by('genre')

    # Розділяємо дані на жанри та доходи
    genres = [entry['genre'] for entry in genres_income]
    income = [entry['total_income'] for entry in genres_income]

    # Створення графіка з Bokeh
    p = figure(title="Income by Genre", x_axis_label='Genre', y_axis_label='Income')
    p.vbar(x=genres, top=income, width=0.5, color="blue")

    # Генерація HTML для графіка
    script, div = components(p)

    return render(request, 'publishing/graph.html', {'script': script, 'div': div})


# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .queries import (
    get_avg_publications_per_author,
    get_books_per_genre,
    get_avg_price_per_publishing_house,
    get_total_income_per_month,
    get_orders_per_status,
    get_avg_books_per_publishing_house
)

@api_view(['GET'])
def avg_publications_per_author(request):
    data = get_avg_publications_per_author()
    return Response(data)

@api_view(['GET'])
def books_per_genre(request):
    data = get_books_per_genre()
    return Response(data)

@api_view(['GET'])
def avg_price_per_publishing_house(request):
    data = get_avg_price_per_publishing_house()
    return Response(data)

@api_view(['GET'])
def total_income_per_month(request):
    data = get_total_income_per_month()
    return Response(data)

@api_view(['GET'])
def orders_per_status(request):
    data = get_orders_per_status()
    return Response(data)

@api_view(['GET'])
def avg_books_per_publishing_house(request):
    data = get_avg_books_per_publishing_house()
    return Response(data)


# views.py
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .queries import (
    get_avg_publications_per_author,
    get_books_per_genre,
    get_avg_price_per_publishing_house,
    get_total_income_per_month,
    get_orders_per_status,
    get_avg_books_per_publishing_house
)

@api_view(['GET'])
def avg_publications_per_author(request):
    data = get_avg_publications_per_author()
    df = pd.DataFrame([data])
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def books_per_genre(request):
    data = get_books_per_genre()
    df = pd.DataFrame(list(data))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def avg_price_per_publishing_house(request):
    data = get_avg_price_per_publishing_house()
    df = pd.DataFrame(list(data))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def total_income_per_month(request):
    data = get_total_income_per_month()
    df = pd.DataFrame(list(data))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def orders_per_status(request):
    data = get_orders_per_status()
    df = pd.DataFrame(list(data))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def avg_books_per_publishing_house(request):
    data = get_avg_books_per_publishing_house()
    df = pd.DataFrame(list(data))
    return Response(df.to_dict(orient='records'))


# views.py
import plotly.express as px
from django.shortcuts import render
from .models import Author, Book
from .analysis import analyze_author_publications
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

def author_publications_graph(request):
    authors = Author.objects.all()
    data = {
        'Author': [f'{author.first_name} {author.last_name}' for author in authors],
        'Number of Publications': [author.number_of_publications for author in authors]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Author', y='Number of Publications', title="Number of Publications by Author")
    graph_html = fig.to_html(full_html=False)
    return render(request, 'author_publications_graph.html', {'graph_html': graph_html})

def income_by_genre(request):
    genres_income = Book.objects.values('genre').annotate(total_income=Sum('price')).order_by('genre')
    df = pd.DataFrame(list(genres_income))
    fig = px.pie(df, values='total_income', names='genre', title="Income by Genre")
    graph_html = fig.to_html(full_html=False)
    return render(request, 'income_by_genre.html', {'graph_html': graph_html})

def income_by_genre_bokeh(request):
    genres_income = Book.objects.values('genre').annotate(total_income=Sum('price')).order_by('genre')
    genres = [entry['genre'] for entry in genres_income]
    income = [float(entry['total_income']) for entry in genres_income]  # Перетворення decimal.Decimal у float
    p = figure(title="Income by Genre", x_axis_label='Genre', y_axis_label='Income')
    p.vbar(x=genres, top=income, width=0.5, color="blue")
    script, div = components(p)
    return render(request, 'publishing/graph.html', {'script': script, 'div': div})

# views.py
import plotly.express as px
from django.shortcuts import render
from .models import Book, PublishingHouse
import pandas as pd
from django.db.models import Avg

def avg_price_per_publishing_house(request):
    avg_prices = Book.objects.values('publishing_house__name').annotate(avg_price=Avg('price')).order_by('publishing_house__name')
    df = pd.DataFrame(list(avg_prices))
    fig = px.line(df, x='publishing_house__name', y='avg_price', title="Average Price per Publishing House")
    graph_html = fig.to_html(full_html=False)
    return render(request, 'avg_price_per_publishing_house.html', {'graph_html': graph_html})

# views.py
import plotly.express as px
from django.shortcuts import render
from .models import Book
import pandas as pd
from django.db.models import Count

def books_per_genre(request):
    genres_count = Book.objects.values('genre').annotate(count=Count('id')).order_by('genre')
    df = pd.DataFrame(list(genres_count))
    fig = px.pie(df, values='count', names='genre', title="Number of Books per Genre")
    graph_html = fig.to_html(full_html=False)
    return render(request, 'books_per_genre.html', {'graph_html': graph_html})

# views.py
import plotly.express as px
from django.shortcuts import render
from .models import Book, PublishingHouse
import pandas as pd
from django.db.models import Count
from django.db.models.functions import TruncMonth

def publications_per_month(request):
    # Отримуємо кількість видань за кожен місяць для кожного видавництва
    publications = (
        Book.objects.annotate(month=TruncMonth('publication_date'))
        .values('month', 'publishing_house__name')
        .annotate(count=Count('id'))
        .order_by('month', 'publishing_house__name')
    )

    # Створюємо DataFrame
    df = pd.DataFrame(list(publications))

    # Створюємо графік
    fig = px.line(df, x='month', y='count', color='publishing_house__name', title="Publications per Month by Publishing House", markers=True)
    fig.update_layout(xaxis=dict(type='category'))
    graph_html = fig.to_html(full_html=False)
    return render(request, 'publications_per_month.html', {'graph_html': graph_html})
