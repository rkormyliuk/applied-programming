# queries.py
from django.db.models import Count, Avg, Sum
from .models import Author, Book, Order, PublishingHouse

# Приклад 1: Середня кількість публікацій на автора
def get_avg_publications_per_author():
    return Author.objects.aggregate(avg_publications=Avg('number_of_publications'))

# Приклад 2: Кількість книг за жанрами
def get_books_per_genre():
    return Book.objects.values('genre').annotate(count=Count('id')).order_by('genre')

# Приклад 3: Середня ціна книг за видавництвами
def get_avg_price_per_publishing_house():
    return Book.objects.values('publishing_house').annotate(avg_price=Avg('price')).order_by('publishing_house')

# Приклад 4: Загальний дохід за місяцями
def get_total_income_per_month():
    return Order.objects.values('order_date__month').annotate(total_income=Sum('total_amount')).order_by('order_date__month')

# Приклад 5: Кількість замовлень за статусами
def get_orders_per_status():
    return Order.objects.values('order_status').annotate(count=Count('id')).order_by('order_status')

# Приклад 6: Середня кількість книг на видавництво
def get_avg_books_per_publishing_house():
    return PublishingHouse.objects.annotate(avg_books=Avg('book__id')).order_by('name')
