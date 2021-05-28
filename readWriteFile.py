def Read(str):
    with open("file.txt",'r') as File:
        content = File.read()
        print(content)
        File.close()
def Write(str):
    total = int(input("How Many to Write ? "))
    Data = []
    for i in range(total):
        insertData = input("Please Insert Data : ")
        Data.append(insertData)
    with open("file.txt",'w') as File:
        for element in Data:
            File.write(element + "\n")
        File.close()
        
wORr = str(input("Read File Type : r \nWrite File Type : w \n"))

if wORr == 'w':
    Write(str)
elif wORr == 'r':
    Read(str)
