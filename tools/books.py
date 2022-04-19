import sqlite3
from tkinter import E
from flask import render_template,request

class Book:

    con=sqlite3.connect('datalibrary.db', check_same_thread=False)   
    cur = con.cursor()

    try:
        cur.execute('''CREATE TABLE Books (ID int,name text,author text,yearpublished int,type int,loanstatus text,unique (ID))''')
    except:
        print("table already created")
    else:
        print("table created sucessfuly")

  
    def addBook(self):
        msg=[]
        if request.method=='POST':
            self.bookid=request.form.get('id')
            self.bookname =request.form.get('name')
            self.author = request.form.get('author')
            self.yearpublished = request.form.get('yearpublished')
            self.type = request.form.get('type')
            try:
                self.cur.execute("INSERT INTO Books (ID,name,author,yearpublished,type) VALUES (?,?,?,?,?)",((self.bookid,self.bookname,self.author,self.yearpublished,self.type)))
                self.cur.execute(f'''UPDATE Books SET loanstatus = 'Available'  WHERE ID={self.bookid}''')
                self.con.commit()
            except:
                msg="book already exists in the library"
            else:
                msg="book added to library"
        return render_template("/books/addBook.html",msg=msg)

    def removeBook(self):
        msg=[]
        if request.method=='POST':
                self.bookid=request.form.get("ID")
                for row in self.cur.execute(f'''SELECT loanstatus from Books WHERE ID={self.bookid} '''):
                    loanstatus=row[0]
                    if(loanstatus == "Available"):
                        self.cur.execute(f"DELETE FROM Books where ID={self.bookid}")
                        self.con.commit()
                        msg="book deleted"
                    else:
                        msg="book can't be deleted becuase it's loaned"
                return render_template("/books/removeBook.html", msg=msg)
        return render_template("/books/removeBook.html",msg=msg)

    def findBook(self):
        if request.method=='POST':
            bookName = request.form.get('bookName')
            self.cur.execute(f'''select * from Books where name like "%{bookName}%"''')
            books = self.cur.fetchall()
            return render_template("/books/findBook.html", books=books)
        return render_template("/books/findBook.html")

    def showAllBooks(self):
        self.cur.execute("SELECT * FROM Books")
        books = self.cur.fetchall()
        return render_template("/books/showAllBooks.html", books=books)