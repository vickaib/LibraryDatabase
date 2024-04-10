class Book:
    # Constructor method for Book superclass
    def __init__(self, genre,name, author, stack_no):
      self.genre = genre
      self.name = name
      self.author = author
      self.stack_no = stack_no

    def get_genre(self):
            return self.genre

    def get_name(self):
            return self.name

    def get_author(self):
            return self.author

    def get_stack_no(self):
            return self.stack_no


class Novel(Book):
    # Constructor method for Novel subclass
    def __init__(self, genre, name, author, stack_no, sub_genre):
            super().__init__(genre, name, author, stack_no)
            self.sub_genre = sub_genre

    def get_sub_genre(self):
            return self.sub_genre

    def __str__(self):
            return "Title: " + self.get_name()+ "\nGenre: " + self.get_genre() \
                       + "\nSub-genre: " + self.get_sub_genre() + "\n\nAuthor: " \
                       + self.get_author() + "\nStack: " +self.get_stack_no()


class Scifi(Book):

    def __init__(self, genre, name, author, stack_no, date = 'No upcoming move', \
                             location = 'No location information'):
            Book.__init__(self, genre, name, author, stack_no)
            self.date = date
            self.location = location

    def get_date(self):
            return self.date

    def get_location(self):
            return self.location

    def __str__(self):
            return "Title: " + self.get_name() + "\nGenre: " + self.get_genre() \
                       + "\nAuthor: " + self.get_author() + "\nStack: " + self.get_stack_no() \
                       + "\nMovie date: " + self.get_date() + " \nLocation: " + self.get_location()


class Book_list(list):
    def search(self,name):
            for book in self:
                    if book.get_name() == name:
                            return book
            return None

def main():

    database = Book_list()   

    try:
        # Read info.txt file
        f = open("info.txt","r")

        # Read info for each book
        for book in f:
            info = book.strip().split(",")

            if info[0] == 'Novel':
                database.append(Novel(info[0], info[1], info[2], info[3], info[4]))

            elif info[0] == 'Scifi':
                if len(info) == 6:
                        database.append(Scifi(info[0], info[1], info[2], info[3], info[4], info[5]))

                else:
                        database.append(Scifi(info[0], info[1], info[2], info[3], info[4]))
        f.close()

        print("----------------------------------------------------------------")
        print("           Welcome to the library database main menu!")
        print("----------------------------------------------------------------")


        while True:

            print("\n\t1. Search\n\t2. Exit")

            choice = int(input("\nEnter choice (1/2): "))

            if choice == 1:
                # Prompt tbe user for the book name to search
                searchBook = input("Enter the title of the book to search: ").strip()

                # Call search method in the extended list class
                book_found = database.search(searchBook)

                # If book is found, print book information
                if not (book_found is None):
                    print("\n----------------------- Book Information -----------------------")
                    print(book_found)
                    print("----------------------------------------------------------------")

                # Otherwise, inform user that the book cannot be not found
                else:
                    print("\nTitle '" + searchBook + "' not found.")
                    print("\nReturning to main menu...")

            # If the user inputs 2, then we will break from the loop
            if choice == 2:
                print("\nThank you for using the Small Book Repository!")
                print("\n\tNow exiting the database...")
                break

            # If library.txt file cannot be found, display a message to the user.
    except IOError:
        print('File not found. Please check the library.txt file to ensure it is in the right folder!')


if __name__=="__main__":
    main()

