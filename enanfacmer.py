from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#function to insert the data in employee table
def insert():
    #take the input for name, dept & salary
    empname = e_empname.get()
    department = e_department.get()
    salary = e_salary.get()
    
    if(department=="" or empname=="" or salary==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        try:
            # connecting to the mysql server
            con = mysql.connect(host="localhost", user="root", password="svis", database="employee_db")
            # cursor object
            custor = con.cursor()
            # ********** INSERT DATA **********
            # insert statement for tblemployee
            custor.execute("INSERT INTO tblemployee (empname,department,salary) VALUES (%s, %s, %s)",(empname,department,salary))
            con.commit()
            # clear the fields
            e_empid.delete(0,'end')
            e_empname.delete (0, 'end')
            e_department.delete (0, 'end')
            e_salary.delete (0, 'end')
            # clear the list
            list.delete (0, 'end')
            # call show function to populate the data in the list
            show()
            MessageBox.showinfo ("Insert Status", "Inserted Successfully")
        except mysql.Error as error:
            MessageBox.showinfo ("Insert Status","Failed to insert into MySQL table {}".format(error))
        finally:
            con.close()

# function to delete the data by employee id
def delete():
    # take the input for the empi id to delete the employee table row by id
    empid = e_empid.get()
    
    if (e_empid.get () == ""):
        MessageBox.showinfo ("Delete Status", "Please enter employee Id")
    else:
        try:
            # connecting to the mysql server
            con = mysql.connect(host="localhost", user="root", password="svis", database="employee_db")
            # cursor object
            cursor = con.cursor()
            # delete statement for tblemployee
            sql_Delete_query = """DELETE FROM tblemployee WHERE empid = %s"""
            # row to delete
            cursor.execute(sql_Delete_query, (empid,))
            con.commit()
            # clear the fields
            e_empid.delete (0, 'end')
            e_empname.delete (0, 'end')
            e_department.delete (0, 'end')
            e_salary.delete (0, 'end')
            # clear the list
            list.delete (0, 'end')
            # call show function to populate the data in the list
            show()
            MessageBox.showinfo ("Delete Status", "Deleted Successfully")
        except mysql.Error as error:
            MessageBox.showinfo ("Delete Status", "Failed to Delete record from table: {}".format(error))
        finally:
            con.close()

# function to update the data by employee id
def update():
    empid = e_empid.get()
    empname = e_empname.get()
    department = e_department.get()
    salary = e_salary.get()
    
    if(empname=="" or department=="" or salary== ""):
        MessageBox.showinfo ("Update Status", "Enter values to be updated")
    else:
        try:
            # connecting to the mysql server
            con = mysql.connect(host="localhost", user="root", password="svis", database="employee_db")
            # cursor object
            cursor = con.cursor()
            # update statement for tblemployee
            sql_update_query = """UPDATE tblemployee SET empname = %s, department = %s, salary=%s WHERE empid = %s"""
            val_update_query = (empname, department,salary, empid )
            cursor.execute(sql_update_query, val_update_query)
            con.commit()
            # clear fields
            e_empid.delete (0, 'end')
            e_empname.delete (0, 'end')
            e_department.delete (0, 'end')
            e_salary.delete (0, 'end')
            # clear the list
            list.delete (0, 'end')
            # call show function to populate the data in the list
            show()
            MessageBox.showinfo ("Update Status", "Updated Successfully")
        except mysql.Error as error:
            MessageBox.showinfo ("Update Status", "Failed to Update record in the table: {}".format(error))
        finally:
            con.close()

#function to select all the employee table data
def get():
    empid = e_empid.get()
    if (empid == ""):
        MessageBox.showinfo("Fetch Status", "Please provide the employee id")
    else:
        try:
            # connecting to the mysql server
            con = mysql.connect(host="localhost", user="root", password="svis", database="employee_db")
            # cursor object
            cursor = con.cursor()
            # select statement for tblemployee as per empid
            sql_select_query = """SELECT * FROM tblemployee WHERE empid = %s"""
            # set variable in query
            cursor.execute(sql_select_query, (empid,))
            # fetch result
            rows = cursor.fetchall()
            for row in rows:
                e_empname.insert (0, row [1])
                e_department.insert (0, row [2])
                e_salary.insert (0, row [3])
                
        except mysql.Error as error:
            MessageBox.showinfo ("Insert Status","Failed to get record from MySQL table: {}".format(error))

        finally:
            con.close()

# function to populate the data in the list
def show ():
    # connecting to the mysql server
    con = mysql.connect(host="localhost", user="root", password="svis", database="employee_db")
    # cursor object
    cursor = con.cursor()
    # select statement for tblemployee which returns all columns
    cursor.execute("SELECT * FROM tblemployee")
    rows = cursor.fetchall ()
    
    for row in rows:
        insertData = str(row [0])+' '+ str(row [1])+' '+ str(row [2])+' '+ str(row [3])
        list.insert(list.size() +1, insertData)
    con.close()
        
root = Tk ()
root.geometry ("600x300")
root.title ("Tkinter Python Program with Database MySql")

# set the position for labels
empid = Label (root, text='Enter empid', font= ('bold', 10))
empid.place (x=20, y=20)

empname = Label (root, text='Enter empname', font= ('bold', 10))
empname.place (x=20, y=40)

department = Label (root, text='Enter department', font= ('bold', 10))
department.place (x=20, y=60)

salary = Label (root, text= 'Enter salary', font= ('bold', 10))
salary.place (x=20, y=80)

emplist = Label (root, text='List of Employees', font= ('bold', 10))
emplist.place (x=300, y=10)

e_empid = Entry ()
e_empid.place (x=150, y=20)

e_empname = Entry ()
e_empname.place (x=150, y=40)

e_department = Entry()
e_department.place (x=150, y=60)

e_salary = Entry()
e_salary.place (x=150, y=80)

insert = Button (root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place (x=20, y=140)

delete = Button (root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place (x=70, y=140)

update = Button (root, text="Update", font=("italic", 10), bg="white", command=update)
update.place (x=130, y=140)

get = Button (root, text="Get", font=("italic", 10), bg="white", command=get)
get.place (x=190, y=140)

# list to show the data
list = Listbox(root)
list.place(x=300, y= 40)
list.config(width=0,height=0)
show()

root.mainloop ()
