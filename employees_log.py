#importing pip modules
import pymongo
import pandas as pa

#connecting to mongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
employees = db.employees

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

#function to update existing document in the collection
def updating_employees():
    ID_upd = int(input("Please enter ID of an employee who need update: "))
    data_existence = db.employees.count_documents({"ID" : ID_upd})
    if data_existence == 0:
        print("Employee with this ID doesn't exist, please try again with different ID.\n")
        employees_log()
    else:
        PhoneNumber_upd = input("Please enter employee's phone number: ")
        Department_upd = input("Please enter employee's department: ")
        Payrate_upd = int(input("Please enter employee's pay-rate per hour: "))
        update = db.employees.update_one(
            {"ID" : ID_upd},
            {"$set" :
                {"PhoneNumber" : PhoneNumber_upd,
                "Department" : Department_upd,
                "Payrate" : Payrate_upd
                }}
        )
        print("Updating employee completed.")
        print(update, "\n")
        viewingall_employees()
        employees_log()

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

#function to create menu to operate CRUD in collection
def employees_log():
    print("Welcome to the Employees Detail Log")
    print("Please enter 1 to view an existing employee.")
    print("Please enter 2 to add new employee.")
    print("Please enter 3 to update an existing employee.")
    print("Please enter 4 to delete an existing employee.")
    print("Please enter 5 to exit out of it.\n")

    choice = int(input("Please choose your entry: "))
    if choice == 1:
        viewing_employees()
    elif choice == 2:
        adding_employees()
    elif choice == 3:
        updating_employees()
    elif choice == 4:
        deleting_employees()
    elif choice == 5:
        exit()
    else:
        print("Invalid entry, please try again.")
        employees_log()
employees_log()



