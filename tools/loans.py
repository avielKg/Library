import sqlite3
from datetime import datetime
from flask import render_template,request


class loans:

    con=sqlite3.connect('datalibrary.db',check_same_thread=False)
    cur=con.cursor()
        
    try:
        cur.execute('''CREATE TABLE Loans (CustID int,BookID int,loandate int,returndate int)''')
    except:
        print("table already created")
    else:
        print("table created sucessfuly")



    def loanabook(self):
        res=[]
        if request.method == "POST":
            self.custid=request.form.get("customerid")
            self.bookid=request.form.get("bookid")
            self.loandate=request.form.get("loandate")
            for row in self.cur.execute(f'''SELECT loanstatus from Books WHERE ID={self.bookid} '''):
                    loanstatus=row[0]
                    if(loanstatus == 'Not Available'):
                        res.append("book isn't available")
                    else:
                        self.cur.execute("INSERT INTO Loans (CustID,BookID,Loandate) VALUES (?,?,?)",(self.custid,self.bookid,self.loandate))
                        self.cur.execute(f"UPDATE Books SET loanstatus ='Not Available' WHERE ID={self.bookid}")
                        self.con.commit()
                        res.append("book is loaned")
                        return render_template("/loans/loanabook.html", res=res)
            return render_template("/loans/loanabook.html", res=res)
        return render_template("/loans/loanabook.html")
  
    def returnabook(self):
        if request.method== "POST":
            self.bookid=request.form.get("bookid")
            self.returndate=datetime.now()
            self.cur.execute(f"DELETE FROM Loans WHERE BookID={self.bookid}")
            self.cur.execute(f'''UPDATE Books SET loanstatus = 'Available'  WHERE ID={self.bookid}''')
            self.con.commit()
            return render_template("/loans/returnabook.html")
        return render_template("/loans/returnabook.html")     

    def displayallloans(self):
        if request.method=='POST':
            pass
        self.cur.execute('''SELECT * FROM Loans''')
        loans = self.cur.fetchall()
        return render_template("/loans/displayallloans.html", loans=loans)

    


    def displaylateloans(self):
        global booktype,row
        dis=[]
        if request.method=='POST':
            self.bookid=request.form.get("bookid")
            for row in self.cur.execute(f'''SELECT Loans.BookID, Books.type, Loans.loandate FROM Loans
                                            INNER JOIN Books ON Loans.BookID = Books.ID
                                            WHERE BookID={self.bookid}'''):
                            
                booktype=row[1]
                mdate1= datetime.now() - datetime.strptime(row[2], "%Y-%m-%d")
                Dtype1= (mdate1).days > 10
                Dtype2= (mdate1).days > 5
                Dtype3= (mdate1).days > 2
                if(booktype == 1 and Dtype1):
                    dis.append(("Book is late by" ,((mdate1).days-10),"days"))
                    return render_template('loans/displaylateloans.html',dis=dis)
                elif(booktype == 2 and Dtype2):
                    dis.append(("Book is late by" ,((mdate1).days-5),"days"))
                    return render_template('loans/displaylateloans.html',dis=dis)
                elif(booktype == 3 and Dtype3):
                    dis.append(("Book is late by" ,((mdate1).days-2),"days"))
                    return render_template('loans/displaylateloans.html',dis=dis)
                else:
                    dis.append(("book isn't late"))
                    return render_template('loans/displaylateloans.html',dis=dis)
        return render_template('loans/displaylateloans.html',dis=dis)
    
    
