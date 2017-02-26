'''
Session 3
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 3 actions: ‘Send a Thank You’ or ‘Create a Report’ or ‘quit’)

Session 4
Use dicts where appropriate
Write a full set of letters to everyone to individual files on disk
See if you can use a dict to switch between the users selections
Try to use a dict and the .format() method to do the letter as one big template – rather than building up a big string in parts.
'''

import pickle

def ShowMenuOptions():
    """Make a function for the code that allows the user to Add a Donor, View a Report, or Print Thank You letters.
    Allow for saving back to the db."""
    print ("""
        WELCOME TO MAILROOM
        Please Select an option:
        1) Add New Donor
        2) View Report
        3) Print Thank You
        3) Save and exit!
        """)
print(ShowMenuOptions())

def load_donordb():
    try:
        with open('mailroom.pickle', 'rb') as db_handle:
            donor_db = pickle.load(db_handle)
    except IOError:
        donor_db = {
            "Ruby": [50, 100],
            "Khloe": [1000, 1500],
            "Sara": [2000, 2500, 3000],
            "Starla": [50]
        }
    return donor_db

def save_donordb(db):
    try:
        with open('mailroom.pickle', 'wb') as db_handle:
            pickle.dump(db, db_handle)
    except IOError:
        raise "Error: Unable to save donor database."

def AddDonor(ToDoItems, NewTask, Priority): # Task 4
    """ Add a new task to the todo list """
    ToDoItems[NewTask] = Priority

def RemoveTask(ToDoItems, Task): # Task 5
    """ Remove a task from the todo list """
    if(Task in ToDoItems):
        del ToDoItems[Task]

def SavetToFile(ToDoItems, FileName): # Task 6
    """Saves data to a file"""
    objFile = open(FileName, "w")
    for strKey, strValue in ToDoItems.items():
        objFile.write(strKey + "," + strValue + "\n")
    objFile.close()

'''

# 1) Create a dictionary of donor data:
dicRow1 = {"ID": 1, "Donor": "Bob Smith", "Amount": "$1000.00"}
dicRow2 = {"ID": 2, "Donor": "Sue Jones", "Amount": "$150.00"}
dicRow3 = {"ID": 3, "Donor": "Joe James", "Amount": "$2500.00"}
lstTable = [dicRow1,dicRow2,dicRow3]
print(lstTable)
# 2) Add code that lets users appends a new row of data.
# 3) Add a loop that lets the user keep adding rows.


#-------------------------------------------------#
# Title: To Do List
# Dev:   mfeliciano
# Date:  07/24/2016
# Desc: This script will open the ToDo.txt file into a python dictionary
#       and allow the user to add or remove items as needed. When finished
#       the user can exit and save the file.
# ChangeLog: mfeliciano, 07/31/16, adding functions and class.
#
#1)	Make a function for the code that loads each row of data you have from the
# ToDo.txt text file into a Python Dictionary and then adds the rows of data to a Python List.

#2)	Make a function for the code that displays the contents of the Python List object to the user.

#3)	Make a function for the code that allows the user to Add or Remove tasks from the list,
#  plus save the tasks in the List tasks-priorities using numbered choices.

#4)	Make a function for the code that saves the data
#  from the table into the Todo.txt file when the program exits.

#5)	Make a Class to hold the functions.
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
gStrFileName = "C:\\Users\\feliciam\\Documents\\_PythonClass\\Module06\\ToDo.txt"  # The name and path of the todo file
gTodoTasks= {} # A dictionary of todo items


#-- Processing --#
def LoadExistingList(FileName):  # Task 1
    """Make a function for the code that loads each row of data you have from the
    ToDo.txt text file into a Python Dictionary and then adds the rows of data to a Python List."""
    lstData = [] # A row of data separated into elements of a list
    dicTable = {} # A dictionary that acts as a 'table' of rows

    objFile = open(FileName, "r")
    for line in objFile:
        strData = line # reading data
        lstData = strData.split(",") # splitting into 2 elements
        dicTable[lstData[0].strip()] = lstData[1].strip()
    objFile.close()
    return dicTable

def DisplayCurrentTodoList(ToDoItems): # Task 2
    """Make a function for the code that displays
    the contents of the Python List object to the user."""
    print("Need to get DONE!: ")  # I wanted a header in my initial display
    print("---------------------------------")  # Decided to break it up with some dashes (start)
    for strKey, strValue in ToDoItems.items():
        print(strKey + " (" + strValue + ")")
    print("---------------------------------") # Breaking up the list (end)


def AddTask(ToDoItems, NewTask, Priority): # Task 4
    """ Add a new task to the todo list """
    ToDoItems[NewTask] = Priority

def RemoveTask(ToDoItems, Task): # Task 5
    """ Remove a task from the todo list """
    if(Task in ToDoItems):
        del ToDoItems[Task]

def SavetToFile(ToDoItems, FileName): # Task 6
    """Saves data to a file"""
    objFile = open(FileName, "w")
    for strKey, strValue in ToDoItems.items():
        objFile.write(strKey + "," + strValue + "\n")
    objFile.close()


#-- Input/Output --#

def Main():
    """Coordinates I/O and actions"""
    global gStrFileName
    global gTodoTasks
    try:
        # When the program starts load data
        # in a text file called ToDo.txt into a dictionary.
        gTodoTasks = LoadExistingList(gStrFileName)

        # Display all tasks to user
        DisplayCurrentTodoList(gTodoTasks)

        # Display a menu of choices to the user
        # and Process user I/0
        while(True):
            ShowMenuOptions()
            strChoice = str(input("Which option would you like to perform? [1 to 3]"))
            if (strChoice == '1'):    # 1) Add a new item.
                strTask = str(input("What is the task?"))
                strPriority = str(input("What is the priority? (high or low)"))
                AddTask(gTodoTasks, strTask, strPriority)
                DisplayCurrentTodoList(gTodoTasks)
                continue
            elif(strChoice == '2'):    # 2) Remove an existing item.
                for strKey, strValue in gTodoTasks.items():
                    print(strKey)
                strKeyToRemove = input("Which task would you like removed?")
                RemoveTask(gTodoTasks, strKeyToRemove)
                DisplayCurrentTodoList(gTodoTasks)
            elif(strChoice == '3'):    # 3) Save and Exit.
                SavetToFile(gTodoTasks, gStrFileName)
                print("Your To Do list has been updated.")  # Message to let user know data has been saved
                break
            else:
                print("Please select either 1, 2, or 3")  # Message in case user enters the incorrect number
                DisplayCurrentTodoList(gTodoTasks)
                continue
    except Exception as error:  # Handles any Python errors
        print("Hmmm somthing isn't right...")
        print("pythons error info: ")
        print(error)


# start the program
Main() # Call the Main function at the start of the script
'''


