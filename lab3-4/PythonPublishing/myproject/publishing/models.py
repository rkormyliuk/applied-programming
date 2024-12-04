from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    number_of_publications = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'author'


class Book(models.Model):
    publishing_house = models.ForeignKey('PublishingHouse', on_delete=models.CASCADE)  # Використовуємо on_delete для визначення поведінки
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)  # Якщо автор буде видалений, автор буде set to NULL
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    language = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.IntegerField()

    class Meta:
        db_table = 'book'


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'order'


class PublishingHouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_of_fundation = models.DateField()
    telephone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'publishing_house'

