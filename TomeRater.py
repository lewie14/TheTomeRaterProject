#**********Tome Rater Project****************

#Needs this for the invalid email check
import re

class InvalidUserEmail(Exception):
    pass

#***************************User class*************************************
class User(object):
	
	#constructor
	def __init__(self, name, email):
		self.name = name
		self.email = email
		#books is an empty dictionary
		self.books = {}
		
		if not User.isValidEmail(self, email):
			raise InvalidUserEmail
		
	#Method returns user email address
	def get_email(self):
		return self.email
		
	#Method to change email address
	def change_email(self, email):
		
		#Is new email valid
		if not User.isValidEmail(self, email):
			raise InvalidUserEmail
		
		self.email = email
		return "Your email has been updated to {email}".format(email = self.email)
		
		
	#Method to return User information
	def __repr__(self):
		return "User {name}, email: {email}, books read {numberofbooks}".format ( name = self.name, email = self.email, numberofbooks =len(self.books))
		
	#Method to check if two users have the same name and email
	def __eq__(self, other_user):
		if self.name == other_user.name and self.email == other_user.email:
			return True
		else:
			return False

	#Method to create a dictionary of book and rating
	def read_book(self, book, rating=None):
		self.books[book]=rating
	
	
	#Method to calculate average rating
	def get_average_rating(self):
		total = 0
		for rating in self.books.values():
			total += rating
		return total/len(self.books)
		
	#Using Python's isValidEmail function ref 
	#https://www.pythoncentral.io/how-to-validate-an-email-address-using-python/
	def isValidEmail(self, email):
		if len(email) > 7:
			return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))

#*******************************Book class*********************************
class Book:
	
	#constructor
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
	#Method return title of book
	def get_title(self):
		return self.title
	
	#Method return isbn of book
	def get_isbn(self):
		return self.isbn
	
	#Method to set an isbn to a book
	def set_isbn(self, isbn):
		self.isbn = isbn
		return "The isbn number has been updated to {isbn}".format (isbn = self.isbn)
		
	#Method to add a valid rating between 0 and 4
	def add_rating(self, rating):
		if rating >-1 and rating <5:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
			
	#Method to check if two books have the same title and isbn
	def __eq__(self, other_book):
		if self.name == other_book.name and self.isbn == other_user.isbn:
			return True
		else:
			return False
           
           
	#Method to calculate average rating
	def get_average_rating(self):
		return sum(self.ratings) / len(self.ratings)
		
	#Method to make sure our object is hashable
	def __hash__(self):
		return hash((self.title, self.isbn))
           
#**************Fiction class which is a subclass of Book*******************
class Fiction(Book):
	
	#constructor
	def __init__(self, title, author, isbn):
		#call parent constructor
		super().__init__(title, isbn)
		self.author = author
		
	#Method to return author
	def get_author(self):
		return self.author
		
	#Method to return author information
	def __repr__(self):
		return "{title} by {author}".format (title = self.title, author = self.author)
        
        
#*************Non-fiction class which is a subclass of Book****************
class Non_Fiction(Book):
	
	#constructor
	def __init__(self, title, subject, level, isbn):
		#call parent constructor
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
		
	#Method to return subject
	def get_subject(self):
		return self.subject
		
	#Method to return level
	def get_level(self):
		return self.level
		
	#Method to return subject information
	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format (title = self.title, level = self.level, subject = self.subject)
		

#********************************Tome Rater Class**************************

class TomeRater:
	
	#constructor
	def __init__(self):
		#Dictionary to map users email to user
		self.users = {}
		#Dictionary to map a Book object to nuber of users who have read it
		self.books = {}
		
	#Method to create a new book
	def create_book(self, title, isbn):
		newBook = Book(title, isbn)
		return newBook
		
	#Method to create a new fiction book
	def create_novel(self, title, author, isbn):
		newFiction = Fiction(title, author, isbn)
		return newFiction
		
	#Method to create new non fiction book
	def create_non_fiction(self, title, subject, level, isbn):
		newNonFiction = Non_Fiction(title, subject, level, isbn)
		return newNonFiction
		
	#Method to add a book to a user
	def add_book_to_user(self, book, email, rating=None):
		if not self.users[email]:
			print("the email address {email} does not match any user.".format(email=email))
		else:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			#if book already in self.books add 1, if not set to 1
			if book in self.books:
				self.books[book] += 1
			else:
				self.books[book] = 1
			
	#Method to make a user object
	def add_user(self, name, email, books=None):
		newUser = User(name, email)
		self.users[newUser.email] = newUser
		if books != None:
			if books is list:
				for book in books:
					self.add_book_to_user(book, email, None)
					
	#Method for printing the books of a user
	def print_catalog(self):
		for book in self.books.keys():
			print(book)
			
	#Method for printing out the users
	def print_users(self):
		for user in self.users.values():
			print(user)
#**************************************************************************		
	#Method to print the most read book
	def most_read_book(self):
		mostReadBook = None
		max_value = 0
		for key, value in self.books.items():
			if value > max_value:
				max_value = value
				mostReadBook = key
		return mostReadBook.get_title()
		
	#Method to find highest rated book
	def highest_rated_book(self):
		max_key = 0
		highestRatedBook = None
		for key, value in self.books.items():
			if key.get_average_rating() > max_key:
				max_key = key.get_average_rating()
				highestRatedBook = key
		return highestRatedBook.get_title() 
		
		
	#method to find highest average rating
	def most_positive_user(self):
		max_value = 0
		positive_user = None
		for value in self.users.values():
			if value.get_average_rating() > max_value:
				max_value = value.get_average_rating()
				positive_user = value
		return positive_user.name
