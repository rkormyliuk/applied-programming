from django.contrib import admin
from .models import PublishingHouse, Order, Book, Author

admin.site.register(PublishingHouse)
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(Author)