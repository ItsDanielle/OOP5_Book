class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self.__num_pages = num_pages
        self.__ISBN = ISBN
        self.__publisher = publisher

    
    def get_num_pages(self):
        return self.__num_pages

    def get_ISBN(self):
        return self.__ISBN

    def get_publisher(self):
        return self.__publisher

    
    def set_num_pages(self, num_pages):
        self.__num_pages = num_pages

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_publisher(self, publisher):
        self.__publisher = publisher