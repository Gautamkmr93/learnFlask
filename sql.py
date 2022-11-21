import sqlite3

#with sqlite3.connect("mydb.db") as connection:
#    c=connection.cursor()
#    c.execute("""drop Table posts""")
    #c.execute("""Create Table posts (Title Text,Description Text)""")
    #c.execute('Insert into posts values("Good","I am fine")')
    #c.execute('Insert into posts values("well","I am well")')


with sqlite3.connect("employee.db") as connection:
    c=connection.cursor()
    c.execute("""Drop Table Emp_Details""")
    c.execute("""Create Table Emp_Details(FirstName Text,LastName Text,Designation Text,Address Text,Pincode varchar,Mobile varchar)""")
    c.execute('Insert into Emp_Details values("Gautam","Kumar","Software Developer","Dighra Rampur Shah","842002","9999999999")')
    c.execute('Insert into Emp_Details values("Kunal","Kumar","Banker","Dighra Rampur Shah","842002","9999999998")')
    c.execute('Insert into Emp_Details values("Kunal","Kumar","Software Developer","Dighra Rampur Shah","842006","9999999988")')
    c.execute('Insert into Emp_Details values("Kunal","Kumar","Banker","Dighra Rampur Shah","842005","9999999888")')
    c.execute('Insert into Emp_Details values("Kunal","Kumar","Software Developer","Dighra Rampur Shah","842004","9999898988")')   