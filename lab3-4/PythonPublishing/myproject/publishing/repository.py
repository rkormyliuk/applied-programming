from typing import List, Optional
from .models import Author, Book, Order, PublishingHouse

class AuthorRepository:
    @staticmethod
    def get_all_authors() -> List[Author]:
        return Author.objects.all()

    @staticmethod
    def get_author_by_id(author_id: int) -> Optional[Author]:
        return Author.objects.filter(id=author_id).first()

    @staticmethod
    def create_author(**kwargs) -> Author:
        return Author.objects.create(**kwargs)

    @staticmethod
    def delete_author(author_id: int) -> None:
        Author.objects.filter(id=author_id).delete()


class BookRepository:
    @staticmethod
    def get_all_books() -> List[Book]:
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id: int) -> Optional[Book]:
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def create_book(**kwargs) -> Book:
        return Book.objects.create(**kwargs)

    @staticmethod
    def delete_book(book_id: int) -> None:
        Book.objects.filter(id=book_id).delete()


class OrderRepository:
    @staticmethod
    def get_all_orders() -> List[Order]:
        return Order.objects.all()

    @staticmethod
    def get_order_by_id(order_id: int) -> Optional[Order]:
        return Order.objects.filter(id=order_id).first()

    @staticmethod
    def create_order(**kwargs) -> Order:
        return Order.objects.create(**kwargs)

    @staticmethod
    def delete_order(order_id: int) -> None:
        Order.objects.filter(id=order_id).delete()


class PublishingHouseRepository:
    @staticmethod
    def get_all_publishing_houses() -> List[PublishingHouse]:
        return PublishingHouse.objects.all()

    @staticmethod
    def get_publishing_house_by_id(ph_id: int) -> Optional[PublishingHouse]:
        return PublishingHouse.objects.filter(id=ph_id).first()

    @staticmethod
    def create_publishing_house(**kwargs) -> PublishingHouse:
        return PublishingHouse.objects.create(**kwargs)

    @staticmethod
    def delete_publishing_house(ph_id: int) -> None:
        PublishingHouse.objects.filter(id=ph_id).delete()
