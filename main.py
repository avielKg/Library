
import tools.books as tb
import tools.customers as tc
import tools.loans as tl
from flask import Flask,render_template


api = Flask(__name__)

@api.route('/')
def main():
    return render_template('homepage.html')

@api.route('/home')
def home():
    return render_template('homepage.html')

@api.route('/books')
def books():
    return render_template('/books/bookshomepage.html')

@api.route("/books/addBook", methods=['GET', 'POST'])
def addBook():
    return tb.Book.addBook(tb.Book)

@api.route("/books/showAllBooks", methods=['GET', 'POST'])
def displayAllBooks():
    return tb.Book.showAllBooks(tb.Book)

@api.route("/books/removeBook",methods=['GET','POST'])
def removeBook():
    return tb.Book.removeBook(tb.Book)

@api.route("/books/findBook",methods=['GET','POST'])
def findbook():
    return tb.Book.findBook(tb.Book)

@api.route('/customers',methods=['GET','POST'])
def customers():
    return render_template('/customers/customershomepage.html')

@api.route("/customers/addCustomer",methods=['GET','POST'])
def addCustomer():
    return tc.Customer.addCustomer(tc.Customer)

@api.route("/customers/removeCustomer",methods=['GET','POST'])
def removeCustomer():
    return tc.Customer.removeCustomer(tc.Customer)

@api.route("/customers/displayAllCustomers",methods=['GET','POST'])
def displayAllCustomers():
    return tc.Customer.displayAllCustomers(tc.Customer)

@api.route("/customers/findCustomer",methods=['GET','POST'])
def findcustomer():
    return tc.Customer.findCustomer(tc.Customer)

@api.route("/loans")
def loans():
    return render_template("/loans/loanhomepage.html")

@api.route("/loans/loanabook", methods=['GET','POST'])
def loanabook():
    return tl.loans.loanabook(tl.loans)

@api.route("/loans/displayallloans",methods=['GET','POST'])
def displayloans():
    return tl.loans.displayallloans(tl.loans)

@api.route("/loans/returnabook",methods=['GET','POST'])
def returnabook():
    return tl.loans.returnabook(tl.loans)

@api.route("/loans/displaylateloans",methods=['GET','POST'])
def displaylateloans():
    return tl.loans.displaylateloans(tl.loans)

if __name__==("__main__"):
    api.run(debug=True,port=9000)