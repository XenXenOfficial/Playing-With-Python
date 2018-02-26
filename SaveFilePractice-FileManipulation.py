import os
import glob
'''
Anything with
try:
except:
is pythons way of catching errors. The following catches in the program
is to make sure that the file actually exists.
'''


d_Letter = os.getcwd() #Grabs the current directory

def file_No_Extension(): #Function to get files without a file extension
    #Borrowed from Keatinge
    files_no_ext = ["\n".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)] #Puts it all on a new line, 
                                                                                             #removes the periods, deletes the extensions 
                                                                                             #for each file printed IF its a file.
    return "\n".join(files_no_ext) #Returns the files in a pretty list

def change_Dir(change): #Change the directory and other things
    check = 'y'
    file_Dir = change
    print(file_Dir)
    while check != 'n':
        print("\nChange directory? (y/n/Type add with a following name to add onto current directory/ ~ to go back)")
        print("Ex. 'add *Folder name*', or type 'List' to view the folders ")
        u_Input = input(">  ")
        if 'List' in u_Input:
            folders = [f for f in os.listdir() if os.path.isdir(f)] #Makes f equal all the current directory folder names
            for i in folders:
                print("\n" + i)
        else:            
            add_Check = []
            add_Check = u_Input.split(" ")
            if 'add' not in add_Check:
                if '~' not in add_Check:
                    if u_Input not in ('y', 'n'):
                        print("\nPlease put a valid answer")
                        continue
                    else:
                        if u_Input in 'y':
                            quitLoop = ''
                            while quitLoop != 'q':
                                temp_Val = file_Dir
                                file_Dir = input("\nWhat do you want it changed to? (q to quit):  ")
                                if file_Dir not in ("\\", 'q'):
                                    file_Dir += "\\" #Adds on the input value
                                    try:
                                        os.chdir(file_Dir)
                                        u_Input = 'n'
                                        quitLoop = 'q'
                                    except FileNotFoundError:
                                        print("That directory doesn't exist!")
                                        continue
                                if file_Dir in 'q': #Checks if there is a quit
                                    continue
                    if 'n' in add_Check: #Checks if a n was sent instead
                        return file_Dir 
                if '~' in add_Check:             
                    file_Dir = os.path.dirname(file_Dir)
                    os.chdir(file_Dir)
                    print("\n" + file_Dir)
            elif 'add' in add_Check:
                try:
                    temp_File_Dir = file_Dir
                    file_Dir = file_Dir + "\\" + add_Check[1]
                    os.chdir(file_Dir)
                    print("\n" + file_Dir)
                except FileNotFoundError:
                    print("That directory doesn't exist!")
                    file_Dir = temp_File_Dir #Gets changed back to the temp value
                    continue

def file_Finder(chosen_File): #Finds a file without a extension
    #Borrowed from Samuele Mattiuzzo
    #Glob finds all the pathnames matching a specified pattern. 
    path = file_Dir
    for infile in glob.glob(os.path.join(path, chosen_File + '.*')): #The pattern? The name of the file is the pattern
                                                                    #and it grabs whatever extension it is.
        return infile #Returns the file extension

def file_Size_Finder(size): #Finds the size of a file 
    #Thanks Blue for teaching me Enumerate and other things
    byte_List = [" B", " MB", " KB", " GB", " TB", " PB"]
    for sVal in byte_List: #Makes SVal go through the list above
        if round(size, 3) > 0: #Checks if the size is greater than 0
            print(round(size, 3), SVal) #Prints it rounded
            size /= 1024 #Divides it by 1024 to get the next file size (If B it'll go to MB
        
file_Dir = change_Dir(d_Letter)


option_List = ["1. List options", 
              " 2. List files with extension", 
              " 3. Create a folder", 
              " 4. Get chosen file size",
              " 5. Create a file",
              " 6. Write to a file",
              " 7. Rename a file" ,
              " 8. Change directory", 
              " 9. Current Directory",
              " ` Advanced creation (Access to Command Prompt)" ]

print("\n What do you want to do? ", '\n\n' , '\n\n'.join(option_List))


while True:
    option = input("> ")    
   
    if option == '1':
        print('\n'.join(option_List)) #Prints the options
    
    elif option == '2':
        print('\n'.join(os.listdir())) #Prints the dir folders and files
   
    elif option == '3':
        f_Name = input("\nFolder name?: ")
        os.makedirs(f_Name) #Creates a folder
   
    elif option == '4':
        print(file_No_Extension()) #Prints the files without a extension
        yn = 'y'
        while yn != 'q':
            chosen_File = input("\nWhat file (q to quit)? ")
            if chosen_File in 'q':
                yn = 'q'
                continue
            try:
                size = 0.0
                chosen_File = file_Finder(chosen_File) #Goes find the file
                size = os.path.getsize(chosen_File) #Gets the file size
            except FileNotFoundError: 
                print("\nFile doesn't exist!")
                continue
            except TypeError:
                print("\nFile doesn't exist!")
                continue
            else:
                file_Size_Finder(size) #Pretty prints it
    elif option == '5':
        while True:
            f_Name_And_Extension = input("\nWhat's the filename and extension you want it to be? ")
            try:
                os.open(f_Name_And_Extension, os.O_RDWR|os.O_CREAT|os.O_EXCL) # os.O_RDWR, os.O_CREAT and os.O_EXCL means get readable and writeable permissions of the file
                                                                           #If it doesn't exist, os.O_CREAT, means create it. and EXCL is just there to make sure
                                                                           #that you don't create a file with the same name.
                break
            except:
                print("\nFile already exists!")
                continue
                
    elif option == '6':
        print(file_No_Extension())
        osF_Write = ''
        while True:
            try:
                f_Name = input("\nTo what file? ")
                text_To_Write = input("\nWhat do you want to write? ")
                f_Name = file_Finder(f_Name) #Finds the file 
                osF_Write = os.open(f_Name, os.O_RDWR) #Open it in the code with Read and Write permissions
            except FileNotFoundError:
                print("\nFile doesn't exist!")
                continue
            else:
                with open(osF_Write, 'a') as f_Name: #Write to the file with whatever you want, the 'a' means 
                                                   #append
                    f_Name.write(text_To_Write)
                    
    elif option == '7':
        print(file_No_Extension())
        print("\nWhat file do you want renamed?")
        file_Name = input("\r> ")
        file_Name = fileFinder(file_Name) #finds the file
        print("\nTo? ")
        file_Rename = input("\r> ")
        try:    
            os.rename(file_Name, file_Rename) #Renames it unless it doesn't exist
        except FileNotFoundError:
            print("\nFile doesn't exist!")
            
    elif option == '8':
        file_Dir = change_Dir(file_Dir) #Goes to the change dir function
        
    elif option == '9':
        print(file_Dir) #Prints the current dir
        
    elif option == "`": #For the more tech savvy people. 
        while True:
            command = input("(` to exit)> ")
            if command == "`":
                break
            os.system(command)
