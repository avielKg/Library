import sqlite3
from flask import Flask,render_template,request


class Customer:
    
    con=sqlite3.connect('datalibrary.db', check_same_thread=False)   
    cur = con.cursor()

    try:
     cur.execute('''CREATE TABLE Customers (
            ID int,name text,city text,age int,
            PRIMARY KEY (ID), unique (ID))''')

    except:
         print("table already created")
    else:
         print("table created sucessfuly")
         
    def addCustomer(self):
            msg="nothing"
            if request.method=='POST':
                self.custmerid=request.form.get("ID")
                self.customername=request.form.get("name")
                self.customercity=request.form.get("city")
                self.customerage=request.form.get("age")
                try:
                    self.cur.execute("INSERT INTO Customers VALUES(?,?,?,?)",(self.custmerid,self.customername,self.customercity,self.customerage))
                    self.con.commit()
                except:
                    msg="user already exists"
                else:
                    msg="user created"
            return render_template("/customers/addCustomer.html",msg=msg)

    def displayAllCustomers(self):
        if request.method=='POST':
            pass
        self.cur.execute('''SELECT * FROM customers''')
        customers = self.cur.fetchall()
        return render_template("/customers/displayAllCustomers.html", customers=customers)


   


    def findCustomer(self):
        if request.method=="POST":
            self.name=request.form.get("name")
            self.cur.execute(f'''SELECT * FROM customers where name like "%{self.name}%"''')
            cust = self.cur.fetchall()
            return render_template("/customers/findCustomer.html", cust=cust)
        return render_template("/customers/findCustomer.html")
    
    def removeCustomer(self):
        if request.method=='POST':
            customername = request.form.get('name')
            self.cur.execute(f'''DELETE FROM customers where name="{customername}"''')
            self.con.commit()
            cRem="Customer removed!"
            goToBookDatabase="Click here"
            goBack="to go back."
            return render_template("/customers/removeCustomer.html", cRem=cRem, goToBookDatabase=goToBookDatabase, goBack=goBack)
        return render_template("/customers/removeCustomer.html")