import os, glob
'''
Anything with
try:
except:
is pythons way of catching errors. The following catches in the program
is to make sure that the file actually exists. Except one special case on line 140.
'''


dLetter = os.getcwd() #Grabs the current directory

def fileNoExtension(): #Function to get files without a file extension
    #Borrowed from Keatinge
    files_no_ext = ["\n".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)] #Puts it all on a new line, 
                                                                                             #removes the periods, deletes the extensions 
                                                                                             #for each file printed IF its a file.
    return "\n".join(files_no_ext) #Returns the files in a pretty list

def changeDir(change): #Change the directory and other things
    check = 'y'
    fileDir = change
    while check != 'n':
        print(fileDir)
        print("\nChange directory? (y/n/Type add with a following name to add onto current directory/ ~ to go back)")
        print("Ex. 'add *Folder name*', or type 'List' to view the folders ")
        uInput = input(">  ")
        if 'List' in uInput:
            for i, i2, i3 in os.walk(fileDir): #This grabs i as a directory path, i2 as directory names, i3 as file names.
                print(i)
        else:            
            addCheck = []
            addCheck = uInput.split(" ")
            if 'add' not in addCheck:
                if '~' not in addCheck:
                    if uInput not in ('y', 'n'):
                        print("\nPlease put a valid answer")
                        continue
                    else:
                        if uInput in 'y':
                            quitLoop = ''
                            while quitLoop != 'q':
                                tempVal = fileDir
                                fileDir = input("\nWhat do you want it changed to? (q to quit):  ")
                                if fileDir not in ("\\", 'q'):
                                    fileDir += "\\" #Adds on the input value
                                    print(fileDir)
                                    try:
                                        os.chdir(fileDir)
                                        uInput = 'n'
                                        quitLoop = 'q'
                                    except FileNotFoundError:
                                        print("That directory doesn't exist!")
                                        continue
                                if fileDir in 'q': #Checks if there is a quit
                                    continue
                    if 'n' in addCheck: #Checks if a n was sent instead
                        return fileDir 
                if '~' in addCheck:             
                    tempList = fileDir.split('\\') #Removes the \ in the filde dir and makes it into a list
                    del tempList[-1] #Deletes the last part of the list 
                    tempList = "\\".join(tempList) #Puts it back together with \
                    fileDir = tempList #Changes the file directory
            elif 'add' in addCheck:
                tempFileDir = fileDir #temp value for file dir
                del addCheck[0] #Deletes the first list value and value [1] gets put into [0]
                fileDir += "\\" + addCheck[0] #Puts the modified value on
                try:
                    os.chdir(fileDir) #Checks if it exists
                except FileNotFoundError:
                    print("That directory doesn't exist!")
                    fileDir = tempFileDir #Gets changed back to the temp value
                    continue

def fileFinder(chosenFile): #Finds a file without a extension
    #Borrowed from Samuele Mattiuzzo
    
    #Glob finds all the pathnames matching a specified pattern. 
    path = fileDir
    for infile in glob.glob(os.path.join(path, chosenFile + '.*')): #The pattern? The name of the file is the pattern
                                                                    #and it grabs whatever extension it is.
        return infile #Returns the file extension

def fileSizeFinder(size): #Finds the size of a file, i don't know how to more efficiently do it 
    if size > 1024:
        size /= 1024
        if size > 1024:
            size /= 1024
            if size > 1024:
                size /= 1024
                if size > 1024:
                    print("Too big!")
                else:
                    print(round(size, 2), " terabytes")
            else:
                print(round(size, 2), " gigabytes")
        else:
            print(round(size, 2), " kilobytes")
    else:
        print(size, " bytes")

fileDir = changeDir(dLetter)


optionList = ["\n 1. List options", "\n 2. List files with extension", "\n 3. Create a folder", "\n 4. Get chosen file size",
             "\n 5. Create a file","\n 6. Write to a file" ,"\n 7. Rename a file" , "\n 8. Change directory", "\n 9. Current Directory",
             "\n ` Advanced creation (Access to Command Prompt)" ]

print("\n What do you want to do? ", '\n' , '\n'.join(optionList))


while True:
    option = input("> ")    
   
    if option == '1':
        print('\n'.join(optionList)) #Prints the options
    
    elif option == '2':
        print('\n'.join(os.listdir())) #Prints the dir folders and files
   
    elif option == '3':
        fName = input("\nFolder name?: ")
        os.makedirs(fName) #Creates a folder
   
    elif option == '4':
        print(fileNoExtension()) #Prints the files without a extension
        yn = 'y'
        while yn != 'q':
            chosenFile = input("\nWhat file (q to quit)? ")
            if chosenFile in 'q':
                yn = 'q'
                continue
            try:
                size = 0.0
                chosenFile = fileFinder(chosenFile) #Goes find the file
                size = os.path.getsize(chosenFile) #Gets the file size
            except FileNotFoundError: 
                print("\nFile doesn't exist!")
                continue
            except TypeError:
                print("\nFile doesn't exist!")
                continue
            else:
                fileSizeFinder(size) #Pretty prints it 
 
    elif option == '5':
        while True:
            fNameAndExtension = input("\nWhat's the filename and extension you want it to be? ")
            try:
                os.open(fNameAndExtension, os.O_RDWR|os.O_CREAT|os.O_EXCL) # os.O_RDWR, os.O_CREAT and os.O_EXCL means get readable and writeable permissions of the file
                                                                           #If it doesn't exist, os.O_CREAT, means create it. and EXCL is just there to make sure
                                                                           #that you don't create a file with the same name.
                                                                        
                break
            except:
                print("\nFile already exists!")
                continue
                
    elif option == '6':
        print(fileNoExtension())
        osFWrite = ''
        while True:
            try:
                fName, textToWrite = input("\nTo what file? "), input("\nWhat do you want to write? ")
                fName = fileFinder(fName) #Finds the file 
                osFWrite = os.open(fName, os.O_RDWR) #Open it in the code with Read and Write permissions
            except FileNotFoundError:
                print("\nFile doesn't exist!")
                continue
            else:
                with open(osFWrite, 'a') as fName: #Write to the file with whatever you want, the 'a' means 
                                                   #append
                    fName.write(textToWrite)
                    
    elif option == '7':
        print(fileNoExtension())
        print("\nWhat file do you want renamed?")
        fileName = input("\r> ")
        fileName = fileFinder(fileName) #finds the file
        print("\nTo? ")
        fileRename = input("\r> ")
        try:    
            os.rename(fileName, fileRename) #Renames it unless it doesn't exist
        except FileNotFoundError:
            print("\nFile doesn't exist!")
            
    elif option == '8':
        fileDir = changeDir(fileDir) #Goes to the change dir function
        
    elif option == '9':
        print(fileDir) #Prints the current dir
        
    elif option == "`": #For the more tech savvy people. 
        while True:
            command = input("(` to exit)> ")
            if command == "`":
                break
            os.system(command)
