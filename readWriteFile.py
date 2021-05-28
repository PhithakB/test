#Description of this Program
#Author : Phithak Buathong
#Since : 2021-05-06
#Program Name : Read & Write File
#Program Language : Python
#Program Purpose : Write a small program

def ReadFile(str):                      #function for Read File
    with open("file.txt",'r') as File:  #this function for open file
        DataInFile = File.read()        #read file and put to DataInFile
        print(DataInFile)               #show data in this file
        File.close()

def AcceptData(str):    #function for Accept File
    pass                #Just pass because not do anything

def ReplaceData(str):                                       #function for Replace Data in File
    total = int(input("How Many to Write ? "))              #set total for get data from Keyboard
    Data = []
    for amount in range(total):                             #this function for read data in total
        insertData = input("Please Insert Data : ")         #this Variable for get data from Keyboard
        Data.append(insertData)                             #this command for put data to Data Variable
    insertFileName = input("Please Insert File Name : ")    #this Variable for get data from Keyboard
    with open(insertFileName+".txt",'w') as File:           #this function for open file
        for element in Data:                                #this function for get data from Data Variable
            File.write(element + "\n")                      #this command for Write data from Data Variable to File
        File.close()

def DeleteData(str):                    #function for Delete Data in File
    with open("file.txt",'w') as File:  #this function for open file
        File.write("")                  #write space to File for delete Data
        File.close()

def AddData(str):                                   #function for Add Data to File
    total = int(input("How Many to Add ? "))        #set total for get data from Keyboard
    Data = []
    for amount in range(total):                     #this function for read data in total
        insertData = input("Please Insert Data : ") #this Variable for get data from Keyboard
        Data.append(insertData)                     #this command for put data to Data Variable
    with open("file.txt",'a') as File:              #this function for open file
        for element in Data:                        #this function for get data from Data Variable
            File.write(element + "\n")              #this command for Add data from Data Variable to File
        File.close()
        
ReadFile(str)   #Rus function ReadFil for show Data in File
SELECT = str(input("Accept Data Type  : acc \n\
Replace Data Type : rep \n\
Delete Data Type  : del \n\
Add Data Type     : add\n\
Type Here         : ")) #this Variable for get data from Keyboard


if SELECT == 'acc':     #this function for compare if get acc from keyboard then run AcceptData Function
    AcceptData(str)
elif SELECT == 'rep':   #this function for compare if get rep from keyboard then run ReplaceData Function
    ReplaceData(str)
elif SELECT == 'del':   #this function for compare if get del from keyboard then run DeleteData Function
    DeleteData(str)
elif SELECT == 'add':   #this function for compare if get add from keyboard then run AddData Function
    AddData(str)

