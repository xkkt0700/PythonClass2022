# ------------------------------------------------------------------------ #
# Title: Assignment05
# Description: Dictionaries
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kristin Temperly, updated script 2/15/22 to complete assignment05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables because Randal says it's a good idea!
strData = ""  # data returned by user
dicRow = {}  # dictionary row
lstTable = []  # list row
strMainMenu = ""  # user menu
strUserChoice = ""  # user menu choice

# -- Processing -- #
# Step 1 - When the program starts, load any data you have just like our lab 5-2

# -- Processing -- #
# Step 1 Load data using dictionary
objFile = open('KristinToDoList.txt', 'r')  # open in read mode
for row in objFile:  # for loop
    strData = row.split(",")  # split by comma
    dicRow = {'Task': strData[0], 'Priority': strData[1]}  # read
    lstTable.append(dicRow)  # append lstTable with each dicRow
objFile.close()  # close the file


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing item
    4) Save Data to File
    5) Exit Program
    """)
    strUserChoice = str(input("Please choose an option 1 to 5: "))
   # Step 3 - display current items in the table
    if strUserChoice == '1':
        for row in lstTable:  # loop thru
            strData1 = row['Task']  # key name
            strData2 = row['Priority']  # key name
            print(strData1 + " | " + strData2)  # print the row separated by a bar
        continue # optional continue
    # Step 4 - Add a new item to the list/Table
    elif strUserChoice == '2':
        strTask = input("Enter Your Task: ")  # user prompt for task
        strPriority = input("Enter Your Priority: ")  # user prompt for priority
        dicRow = {'Task': strTask, 'Priority': strPriority}  # create a new dicRow with new task
        lstTable.append(dicRow)  # append dicRow to table
        continue # optional continue
    # Step 5 - Remove a new item from the list/Table
    elif strUserChoice == '3':
        deleteChoice = input("Which Task Would You Like To Remove? ")  # user prompt for deletion
        for row in range(len(lstTable)):  # loop thru each row of the lstTable
            if lstTable[row]['Task'] == deleteChoice:  # look for delete choice
                del lstTable[row]  # delete the row
                break  # break the if loop
        continue #optional continue
    # Step 6 - Save to KristinToDoToDoList.txt file
    elif strUserChoice == '4':
        objFile = open('KristinToDoList.txt', 'w')  # write to file
        for row in lstTable:  # loop lstTable
            strData1 = row['Task']  # pull task value from lstTable
            strData2 = row['Priority']  # pull priority value from lstTable
            objFile.write(strData1 + ',' + strData2)  # write tasks and priorities to file
        objFile.close()
        continue # optional continue
    # Step 7 - Exit program
    elif strUserChoice == '5':
        print("You have chosen to exit the program")
        break  # exit