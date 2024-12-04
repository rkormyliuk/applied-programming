from django.urls import path
from django.urls import path
from . import views
from django.urls import path
from .views import (
    PublishingHouseListCreateView,
    PublishingHouseRetrieveUpdateDeleteView,
    AuthorListCreateView,
    AuthorRetrieveUpdateDeleteView,
    OrderListCreateView,
    OrderRetrieveUpdateDeleteView,
    BookListCreateView,
    BookRetrieveUpdateDeleteView, AuthorRegistrationView, AuthorLoginView, login_author, register_author,
)
urlpatterns = [
    # Author URLs
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:pk>/update/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),

    # PublishingHouse URLs
    path('publishinghouses/', views.publishinghouse_list, name='publishinghouse_list'),
    path('publishinghouses/<int:pk>/', views.publishinghouse_detail, name='publishinghouse_detail'),
    path('publishinghouses/create/', views.publishinghouse_create, name='publishinghouse_create'),
    path('publishinghouses/<int:pk>/update/', views.publishinghouse_update, name='publishinghouse_update'),
    path('publishinghouses/<int:pk>/delete/', views.publishinghouse_delete, name='publishinghouse_delete'),

    # PublishingHouse endpoints
    path('api/publishinghouses/', PublishingHouseListCreateView.as_view(), name='publishinghouse-list-create'),
    path('api/publishinghouses/<int:pk>/', PublishingHouseRetrieveUpdateDeleteView.as_view(), name='publishinghouse-detail'),

    # Author endpoints
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:pk>/', AuthorRetrieveUpdateDeleteView.as_view(), name='author-detail'),

    # Order endpoints
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDeleteView.as_view(), name='order-detail'),

    # Book endpoints
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),


    path('api/register/', AuthorRegistrationView.as_view(), name='author_register'),
    path('api/login/', AuthorLoginView.as_view(), name='author_login'),

    path('register/', register_author, name='register_author'),
    path('login/', login_author, name='login_author'),

    path('author_publications_graph/', views.author_publications_graph, name='author_publications_graph'),


    path('author_publications_graph1/', views.author_publications_graph, name='author_publications_graph'),
    path('income_by_genre/', views.income_by_genre, name='income_by_genre'),
    path('income_by_genre_bokeh/', views.income_by_genre_bokeh, name='income_by_genre_bokeh'),
    path('api/avg_publications_per_author/', views.avg_publications_per_author, name='avg_publications_per_author'),
    path('api/books_per_genre/', views.books_per_genre, name='books_per_genre'),
    path('api/avg_price_per_publishing_house/', views.avg_price_per_publishing_house, name='avg_price_per_publishing_house'),
    path('api/total_income_per_month/', views.total_income_per_month, name='total_income_per_month'),
    path('api/orders_per_status/', views.orders_per_status, name='orders_per_status'),
    path('api/avg_books_per_publishing_house/', views.avg_books_per_publishing_house, name='avg_books_per_publishing_house'),

    path('income_by_genre/', views.income_by_genre, name='income_by_genre'),
    path('income_by_genre_bokeh/', views.income_by_genre_bokeh, name='income_by_genre_bokeh'),
    path('avg_price_per_publishing_house/', views.avg_price_per_publishing_house, name='avg_price_per_publishing_house'),
    path('books_per_genre/', views.books_per_genre, name='books_per_genre'),
    path('publications_per_month/', views.publications_per_month, name='publications_per_month'),
]



