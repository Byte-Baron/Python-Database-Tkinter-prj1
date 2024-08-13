import mysql.connector as msc
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Database App")
root.geometry("400x350")
root.resizable(False, False)

db = msc.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
    )

x = db.cursor()


x.execute("create database if not exists python")
x.execute("create table if not exists Student (ID int primary key auto_increment,Name varchar(15), Familly varchar(15))")
x.execute("create table if not exists Info (ID int primary key auto_increment,Phone int, City varchar(20), Address varchar(35), Std_id int, foreign key (Std_id) references Student(ID))")

#Insert data into the database
def insert_data(name, family, phone, city, address):
    try:
        x.execute("insert into Student (Name, Familly) values (%s, %s)", (name, family))
        x.execute("insert into Info (Phone, City, Address, Std_id) values (%s, %s, %s, LAST_INSERT_ID())", (phone, city, address))
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
        update_listbox()
    except:
        messagebox.showerror("Error", "Error inserting data!")

#Update the list box
def update_listbox():
    x.execute("Select Student.Name,Student.Familly,Info.Phone,Info.Address,Info.city from Student join Info on Student.ID=Info.Std_id order by Student.Name")
    z = x.fetchall()
    data_listbox.delete(0, END)
    for row in z:
        data_listbox.insert(END, f"{row[0]} {row[1]} - {row[2]} - {row[3]} - {row[4]}")

#----------------------------------------#
name_label = Label(root, text="Name :")
name_label.place(x=50,y=10)
name_entry = Entry(root,width=18)
name_entry.place(x=103,y=12)

family_label = Label(root, text="Family :")
family_label.place(x=50,y=35)
family_entry = Entry(root,width=18)
family_entry.place(x=103,y=37)

phone_label = Label(root, text="Phone :")
phone_label.place(x=50,y=60)
phone_entry = Entry(root,width=18)
phone_entry.place(x=103,y=62)

city_label = Label(root, text="City :")
city_label.place(x=55,y=85)
city_entry = Entry(root,width=10)
city_entry.place(x=103,y=87)

address_label = Label(root, text="Address :")
address_label.place(x=48,y=110)
address_entry = Entry(root,width=30)
address_entry.place(x=103,y=112)

#Button
insert_button = Button(root, text="Insert",width = 10 , command=lambda: insert_data(name_entry.get(), family_entry.get(), int(phone_entry.get()), city_entry.get(), address_entry.get()))
insert_button.place(x=165,y=140)

#List box
data_listbox = Listbox(root ,width=50)
data_listbox.place(x=50,y=170)

#Update the list box
update_listbox()


root.mainloop()


#Todo ==> 0 in the phone section /auto_increment
