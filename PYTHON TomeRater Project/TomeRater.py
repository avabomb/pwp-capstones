class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        return "Email has be updated to {}".format(self.email)

    def __repr__(self):
        print ("User: {}, Email: {}, books read: {}".format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        return (self.name == other_user.name) and (self.email == other_user.email)

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        for book in self.books.values():
            if book:
                average += book
        average = average/len(self.books.values())
        return average


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("The new ISBN is {}".format(self.isbn))

    def add_rating(self, rating = None):
        if rating:
            if (rating<0) and (rating>4):
                print ("Invalid Rating")
            else:
                self.ratings.append(rating)

    def __eq__(self, other_book):
        return (self.title == other_book.title) and (self.isbn == other_book.isbn)


    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            average+=rating
        average = average/len(self.ratings)
        return average

    def __repr__(self):
        return self.title

    def	__hash__(self):
        return	hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_non = Fiction(title, author, isbn)
        return new_non

    def create_non_fiction(self, title, subject, level, isbn):
        new_nf = Non_Fiction(title, subject, level, isbn)
        return new_nf

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book]+=1
            book.add_rating(rating)
        else:
            return "User does not exist"

    def add_user(self, name, email, books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if books:
            for i in books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books:
            print(i)

    def print_users(self):
        for user in self.users:
            print(user)


    def most_read_book(self):
        return max(self.books)

    def highest_rated_book(self):
        highest_rating = float("-inf")
        best_book = None

        for i in self.books:
            avg = i.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                best_book = i

        return best_book


    def most_positive_user(self):
        highest_avg_rating = 0
        highest_name = " "

        for user in self.users.values():
            average = user.get_average_rating()
            if  average > highest_avg_rating:
                highest_avg_rating = average
                highest_name = user.name

        return("{} with average rating of {}".format(highest_name, highest_avg_rating))


    def get_user_average_rating(self, email):
        user = self.users.get(email, None)
        if user:
            return user.get_average_rating()
        return "User does not exist"

    def get_most_read_book(self):
        high_read_count = 0
        high_read_name = ""
        for book in self.books.keys():
            if self.books[book] > high_read_count:
                high_read_count = self.books[book]
                high_read_name = book.title

        return high_read_name
