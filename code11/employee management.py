#PythonProgramForBasicEmployeeManagementSystem
# File name: ...\\MyPythonXII\Unit1\PyChap\stmenu.py

import os

filename = "Employee.txt" 

def employee_entry(filename):

    fileobj = open(filename, 'a')

    if not fileobj:

        print ("File does not created")

    else:

        ch ='Y'

        print("Enter employee information")

        while ch=='Y' or ch=='y':
            
            employeeno = input("Enter employee no.: ")

            name = raw_input("Enter name: ")

            address = raw_input("Enter address: ")

            # Write record using a comma separator after first field employeeno

            fileobj.write(str(employeeno) + ", " + name.upper() + " - " + address + "\n")    

            ch =raw_input("Do you want more entry? <y/n>: ")

            if ch=='y' or ch=='Y':

                continue

            else:

                break

    fileobj.close()


def employee_read(filename):

    if os.path.isfile(filename):

        fileobj = open(filename,'r')

        print ("Employee information")

        print ("-------------------")

        for Employee in fileobj: # Process till EOF

            print (Employee)#, end="")

        fileobj.close()

    else:

        print ("File does not exist.")



        
def employee_search(filename):

    if os.path.isfile(filename):

        fileobj = open(filename,"r")

        employeeno = int(input("Enter employee no. to search: "))

        flag = False # To check if record not found

        for Employee in fileobj:

            Strlen = len(Employee)

            i = 0

            StrEmployeeno = ""

            while True:

                if Employee[i] == ',': # loop will break after finding first comma.

                    break

                # Extracting numbers from Employee for employeeno.

                if Employee[i] >= '0' and Employee[i] <= '9':

                    StrEmployeeno = StrEmployeeno + Employee[i]

                    i += 1

            Nemployeeno = int(StrEmployeeno) # Str object converted into integer type

            # Checks if the entered employee number match with file data

            if employeeno == Nemployeeno: 

                print ("Employee found: ", Employee)#, end="")

                flag = True

                break

        fileobj.close()

        if flag == False:

            print ("Record does not found.")

    else:

        print ("File does not exist.")

def delrecord(filename):

    fin=open(filename,"r")

    fout=open("temp.txt","w")

    a=int(raw_input("Enter the no. of record to be deleted : "))

    count=0

    rec=" "

    while rec :

        rec=fin.readline()

        count=count+1

        if count==a:

            pass

        else:

            fout.write(rec)

    fin.close()

    fout.close()

    os.remove(filename)

    os.rename("temp.txt",filename)
        
def modifyrecord(filename):

    eno=int(raw_input("Enter employee no. : "))

    fh=open(filename,"r")

    fo=open("temp.txt","w")

    employeeno="3"

    rec=" "

    while rec !="":

        rec=fh.readline()

        if rec.find(employeeno,0,2)!= -1:

            # Record = rec.split(',')

            print "Record right now contains this information : ",rec

            print "Enter new information below : "

            name=raw_input("Enter name : ")

            address=raw_input("Enter address : ")

            fo.write(str(employeeno) + ", " + name.upper() + " - " + address + "\n")

        else:

            fo.write(rec)

    fh.close()

    fo.close()

    os.remove(filename)

    os.rename("temp.txt",filename)

def getChoice(menu):

    print (menu)

    choice = int(input("Select a choice(1-6): "))

    return choice


def main():
    
    theMenu = '''
    Employee Menu
    - - - - - - - -
    1) Add new employee
    2) Display employee details
    3) Search employee
    4) Modify any record
    5) Delete a record
    6) Quit and save
    '''
    choice = getChoice(theMenu)

    while choice != 6:

        if choice == 1:

            employee_entry(filename)

        elif choice == 2:

            employee_read(filename)

        elif choice == 3:

            employee_search(filename)

        elif choice == 4:

            modifyrecord(filename)

        elif choice == 5:

            delrecord(filename)    

        else: print ("Invalid choice, try again")

        choice = getChoice(theMenu)

if __name__ == "__main__":

    main()

