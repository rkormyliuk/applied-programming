# Таблиця 1: publishing_house
class PublishingHouse:
    def __init__(self, id, name, location, year_of_fundation, published, telephone_number, website):
        self.id = id
        self.name = name
        self.location = location
        self.year_of_fundation = year_of_fundation
        self.published = published
        self.telephone_number = telephone_number
        self.website = website

    def get_info(self):
        return f"Видавництво: {self.name}, Розташування: {self.location}, Рік заснування: {self.year_of_fundation}"

# Таблиця 2: book
class Book:
    def __init__(self, id, publishing_house_id, name, author_id, genre, publication_date, language, numbes_of_pages, format, price, date_added_to_sale, distributor, avaiability):
        self.id = id
        self.publishing_house_id = publishing_house_id
        self.name = name
        self.author_id = author_id
        self.genre = genre
        self.publication_date = publication_date
        self.language = language
        self.numbes_of_pages = numbes_of_pages
        self.format = format
        self.price = price
        self.date_added_to_sale = date_added_to_sale
        self.distributor = distributor
        self.avaiability = avaiability

    def get_book_info(self):
        return f"Книга: {self.name}, Жанр: {self.genre}, Мова: {self.language}"

# Таблиця 3: book_list
class BookList:
    def __init__(self, book_id, order_id):
        self.book_id = book_id
        self.order_id = order_id

# Таблиця 4: collaboration
class Collaboration:
    def __init__(self, publishing_house_id, illustrator_id, distributor_id, editor_id):
        self.publishing_house_id = publishing_house_id
        self.illustrator_id = illustrator_id
        self.distributor_id = distributor_id
        self.editor_id = editor_id

    def get_collaboration_info(self):
        return f"Співпраця видавництва {self.publishing_house_id} з ілюстратором {self.illustrator_id}, розповсюджувачем {self.distributor_id} та редактором {self.editor_id}"

# Таблиця 5: author
class Author:
    def __init__(self, id, first_name, second_name, biography, date_of_birth, nationality, number_of_publications, genre):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.biography = biography
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.number_of_publications = number_of_publications
        self.genre = genre

    def get_author_info(self):
        return f"Автор: {self.first_name} {self.second_name}, Національність: {self.nationality}, Жанр: {self.genre}"

# Таблиця 6: order
class Order:
    def __init__(self, id, customer_id, order_date, order_status, total_amount):
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date
        self.order_status = order_status
        self.total_amount = total_amount

    def get_order_info(self):
        return f"Замовлення #{self.id}, Статус: {self.order_status}, Сума: {self.total_amount}"

# Таблиця 7: editor
class Editor:
    def __init__(self, id, first_name, second_name, telephone_number, specialization, edited_books_count):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.telephone_number = telephone_number
        self.specialization = specialization
        self.edited_books_count = edited_books_count

    def get_editor_info(self):
        return f"Редактор: {self.first_name} {self.second_name}, Спеціалізація: {self.specialization}"

# Таблиця 8: customer
class Customer:
    def __init__(self, id, first_name, second_name, telephone_number):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.telephone_number = telephone_number

    def get_customer_info(self):
        return f"Клієнт: {self.first_name} {self.second_name}, Телефон: {self.telephone_number}"

# Таблиця 9: illustrator
class Illustrator:
    def __init__(self, id, first_name, second_name, style, works_count, collaboration):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.style = style
        self.works_count = works_count
        self.collaboration = collaboration

    def get_illustrator_info(self):
        return f"Ілюстратор: {self.first_name} {self.second_name}, Стиль: {self.style}"

# Таблиця 10: distributor
class Distributor:
    def __init__(self, id, name, telephone_number, location, distribution_type, list_of_books):
        self.id = id
        self.name = name
        self.telephone_number = telephone_number
        self.location = location
        self.distribution_type = distribution_type
        self.list_of_books = list_of_books

    def get_distributor_info(self):
        return f"Розповсюджувач: {self.name}, Тип: {self.distribution_type}, Місцезнаходження: {self.location}"

# Демонстрація роботи класів
def demo():
    # Створення екземплярів
    ph = PublishingHouse(1, "Київське Видавництво", "Київ", 1995, "Видано", "+380123456789", "www.publisher.ua")
    book = Book(1, 1, "Моя Книга", 1, "Фантастика", "2022-01-01", "Українська", 300, "М'яка обкладинка", 150.00, "2023-10-01", "Розповсюджувач А", True)
    author = Author(1, "Іван", "Франко", "Відомий письменник", "1856-08-27", "Українець", 100, "Фантастика")
    order = Order(1, 2, "2024-10-01 12:00", "Виконано", 200.00)
    editor = Editor(1, "Олена", "Шевченко", "+380987654321", "Фантастика", 50)
    customer = Customer(1, "Петро", "Коваль", "+380963214789")
    illustrator = Illustrator(1, "Анна", "Гончар", "Реалізм", 30, "Співпраця з видавництвом")
    distributor = Distributor(1, "Книжковий Світ", "+380953214567", "Київ", "Оптова", "Список книг")

    ph1 = PublishingHouse( 2, "Львівське Видавництво", "Львів", 1968, "Видано", "+380123456789", "www.lviv.publishing.ua")
    book1 = Book(2, 2, "Підкова", 1, "Фантастика", "1989", "Українська", 152, "М'яка обкладинка", 150.00, "2024-10-22", "Розповсюджувач А", True)
    author1 = Author(2, "Андрій", "Чума", "Відомий письменник", "1945-08-01", "Українець", 1295, "Фантастика")
    order1 = Order(2, 2, "2024-10-01 12:00", "Виконано", 200.00)
    editor1 = Editor(2, "Вікторія", "Пасічко", "+380985859066", "Фантастика", 50)
    customer1 = Customer(2, "Петро", "Щур", "+380963214789")
    illustrator1 = Illustrator(2, "Роман", "Кормилюк", "Реалізм", 39, "Співпраця з видавництвом")
    distributor1 = Distributor(2, "Книжковий Світ", "+380953214567", "Львів", "Оптова", "Список книг")

    # Виклик методів
    print(ph.get_info())
    print(book.get_book_info())
    print(author.get_author_info())
    print(order.get_order_info())
    print(editor.get_editor_info())
    print(customer.get_customer_info())
    print(illustrator.get_illustrator_info())
    print(distributor.get_distributor_info())

    print(ph1.get_info())
    print(book1.get_book_info())
    print(author1.get_author_info())
    print(order1.get_order_info())
    print(editor1.get_editor_info())
    print(customer1.get_customer_info())
    print(illustrator1.get_illustrator_info())
    print(distributor1.get_distributor_info())

# Запуск демонстрації
demo()
