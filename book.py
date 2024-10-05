import json
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn, page_count):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._page_count = page_count

    @abstractmethod
    def read_page(self):
        pass

    @abstractmethod
    def bookmark_page(self, page):
        pass

    def get_info(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, {self.page_count} pages"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._page_count = value

class EBook(Book):
    def __init__(self, title, author, isbn, page_count, file_size):
        super().__init__(title, author, isbn, page_count)
        self._file_size = file_size

    def read_page(self):
        return "kitbo o'qish"

    def bookmark_page(self, page):
        return f"kitobdan belgilash {page}"

    def download(self):
        return f"ko'chirib olish {self.title}."

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value

class AudioBook(Book):
    def __init__(self, title, author, isbn, page_count, duration):
        super().__init__(title, author, isbn, page_count)
        self._duration = duration

    def read_page(self):
        return "kitobni eshitish"

    def bookmark_page(self, page):
        return f"audioni belgilash{page}."

    def play(self):
        return f"qo'yilmoqda {self.title}."

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
