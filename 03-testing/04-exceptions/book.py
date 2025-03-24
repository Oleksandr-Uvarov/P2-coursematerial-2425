class Book:
    def __init__(self, title, isbn):
        if title == "":
            raise RuntimeError("Title cannot be empty")
        self.__title = title

        digits = []
        for i in range(len(isbn)):
            if isbn[i].isdigit():
                digits.append(int(isbn[i]))
        
        for i in range(len(digits)):
            if i % 2 != 0:
                digits[i] *= 3
        
        if sum(digits) == 0 or sum(digits) % 10 != 0 or len(digits) != 13:
            raise RuntimeError("Wrong ISBN")

        self.__isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    


book = Book('Watchmen', '978-1779501127')
print(book.title)