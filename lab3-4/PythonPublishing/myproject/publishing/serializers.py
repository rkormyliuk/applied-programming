from rest_framework import serializers
from . models import PublishingHouse, Author, Order, Book
class PublishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'nationality', 'number_of_publications', 'genre']

class AuthorLoginSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        try:
            author = Author.objects.get(first_name=first_name, last_name=last_name)
        except Author.DoesNotExist:
            raise serializers.ValidationError("Author not found with the provided credentials.")

        return author
