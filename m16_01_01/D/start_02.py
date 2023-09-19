class PDFBook:
    def read(self):
        return "Reading a PDF Book..."


class EBookReader:
    def __init__(self):
        self.book = PDFBook()

    def read(self):
        return self.book.read()
