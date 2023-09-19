from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def read(self):
        ...


class PDFBook(Book):
    def read(self):
        return "Reading a PDF Book..."


class EBookReader:
    def __init__(self, book: Book):
        self.book = book

    def read(self):
        return self.book.read()
