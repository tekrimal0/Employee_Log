#importing pip modules
import pymongo
import pandas as pa

#connecting to mongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
logins = db.logins
employees = db.employees

#function to create new login
def create_login():
    new_user = input("Please create new username: ")
    login_availability = db.logins.count_documents({"Username" : new_user})
    if login_availability == 1:
        print("Username already exist, please try creating with different username.\n")
        create_login()
    else:
        new_password = input("Please create new password: ")
        new_login = db.logins.insert_one({"Username": new_user, "Password": new_password})
        print("Login created successfully.\n")
        print(new_login, "\n")
        login_menu()

#function to log into the dashbord
def existing_login():
    user_in = input("Please enter your username: ")
    user_existence = db.logins.count_documents({"Username": user_in})
    if user_existence == 0:
        print("Username doesn't exist, please try again.\n")
        existing_login()
    else:
        password_in = input("Please enter your password: ")
        password_existence = db.logins.count_documents({"Password": password_in})
        if password_existence == 0:
            print("Incorrect password, please try logging again.\n")
            existing_login()
        else:
            print("Login successful.\n")
            employees_log()

#function to get the list of the documents present in mongoDB collection
def viewingall_employees():
    viewall = (list(db.employees.find({})))
    print("Here are all the detail list including changes: \n")
    clean_view = pa.DataFrame(viewall)
    print(clean_view, "\n")

#function to view selected document from the collection
def viewing_employees():
    employeeID = int(input("Please enter employeeID who you want to view:  "))
    data_existence = db.employees.count_documents({"ID" : employeeID})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        employees_log()
    else:
        detail = db.employees.find_one({"ID": employeeID})
        print("Here is the detail of an employee of selection: \n")
        clean_detail = pa.Series(detail)
        print(clean_detail, "\n")
        employees_log()

#function to add new document into the collection
def adding_employees():
    ID_in = int(input("Please enter employeeID who you want to add: "))
    data_existence = db.employees.count_documents({"ID" : ID_in})
    if data_existence == 1:
        print("Employee with this ID already exist, please try adding with different ID.\n")
        employees_log()
    else:
        Name_in = input("Please enter employee's full name: ")
        PhoneNumber_in = input("Please enter employee's phone number: ")
        Department_in = input("Please enter employee's department: ")
        Payrate_in = int(input("Please enter employee's pay-rate per hour: "))
        addition = db.employees.insert_one({
            "ID" : ID_in,
            "Name" : Name_in,
            "PhoneNumber" : PhoneNumber_in,
            "Department" : Department_in,
            "Payrate" : Payrate_in })
        print("Adding employee completed.")
        print(addition, "\n")
        viewingall_employees()
        employees_log()

#functions to update one particular document at a time
def update_fullname():
    ID_upd = int(input("Please enter ID of an employee who need update: "))
    data_existence = db.employees.count_documents({"ID" : ID_upd})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        update_menu()
    else:
        FullName_upd = input("Please enter employee's updated full name: ")
        update = db.employees.update_one(
            {"ID" : ID_upd},
            {"$set" :
                {"Name" : FullName_upd
                }}
        )
        print("Updating employee's name completed.")
        print(update, "\n")
        viewingall_employees()
        update_menu()

def update_phonenumber():
    ID_upd = int(input("Please enter ID of an employee who need update: "))
    data_existence = db.employees.count_documents({"ID" : ID_upd})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        update_menu()
    else:
        PhoneNumber_upd = input("Please enter employee's updated phone number: ")
        update = db.employees.update_one(
            {"ID" : ID_upd},
            {"$set" :
                 {"PhoneNumber" : PhoneNumber_upd
                  }}
        )
        print("Updating employee's phone number completed.")
        print(update, "\n")
        viewingall_employees()
        update_menu()

def update_department():
    ID_upd = int(input("Please enter ID of an employee who need update: "))
    data_existence = db.employees.count_documents({"ID" : ID_upd})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        update_menu()
    else:
        Department_upd = input("Please enter employee's updated department: ")
        update = db.employees.update_one(
            {"ID" : ID_upd},
            {"$set" :
                 {"Department" : Department_upd
                  }}
        )
        print("Updating employee's department completed.")
        print(update, "\n")
        viewingall_employees()
        update_menu()

def update_payrate():
    ID_upd = int(input("Please enter ID of an employee who need update: "))
    data_existence = db.employees.count_documents({"ID" : ID_upd})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        update_menu()
    else:
        Payrate_upd = int(input("Please enter employee's updated payrate: "))
        update = db.employees.update_one(
            {"ID" : ID_upd},
            {"$set" :
                 {"Payrate" : Payrate_upd
                  }}
        )
        print("Updating employee's payrate completed.")
        print(update, "\n")
        viewingall_employees()
        update_menu()

#funtion to delete existing document from the collection
def deleting_employees():
    ID_del = int(input("Please enter ID of an employee who need deletion: "))
    data_existence = db.employees.count_documents({"ID" : ID_del})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        employees_log()
    else:
        deletion = db.employees.delete_one({"ID": ID_del})
        print("Deleting employee completed.")
        print(deletion, "\n")
        viewingall_employees()
        employees_log()

#function to create menu for update
def update_menu():
    print("Please enter 1 to update FullName.")
    print("Please enter 2 to update PhoneNumber.")
    print("Please enter 3 to update Department.")
    print("Please enter 4 to update Payrate.")
    print("Please enter 5 to go back to the dashboard.\n")

    update_choice = int(input("Please choose your entry: "))
    if update_choice == 1:
        update_fullname()
    elif update_choice == 2:
        update_phonenumber()
    elif update_choice == 3:
        update_department()
    elif update_choice == 4:
        update_payrate()
    elif update_choice == 5:
        employees_log()
    else:
        print("Invalid entry, please try again.\n")
        update_menu()

#function to create menu to operate CRUD in collection
def employees_log():
    print("Welcome to the EmployeesLog Dashboard!")
    print("Please enter 1 to view an existing employee.")
    print("Please enter 2 to add new employee.")
    print("Please enter 3 to update an existing employee.")
    print("Please enter 4 to delete an existing employee.")
    print("Please enter 5 to log out and go back to login page.")
    print("Please enter 6 to exit out of it.\n")

    choice = int(input("Please choose your entry: "))
    if choice == 1:
        viewing_employees()
    elif choice == 2:
        adding_employees()
    elif choice == 3:
        update_menu()
    elif choice == 4:
        deleting_employees()
    elif choice == 5:
        login_menu()
    elif choice == 6:
        exit()
    else:
        print("Invalid entry, please try again.\n")
        employees_log()

#function to create menu for login page
def login_menu():
    print("Welcome to login page for EmployeeLog ")
    print("Please enter 1 to login into the EmployeeLog.")
    print("Please enter 2 to create login credentials.")
    print("Please enter 3 to exit out of it.\n")

    login_choice = int(input("Please choose your entry: "))
    if login_choice == 1:
        existing_login()
    elif login_choice == 2:
        create_login()
    elif login_choice == 3:
        exit()
    else:
        print("Invalid entry, please try again!")
        login_menu()
login_menu()


