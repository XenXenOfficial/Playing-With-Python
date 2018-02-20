import sys
stringVal = input("\nPut in a string to mess around with> ")
stringVal = str.capitalize(stringVal)

def StringSplitter(): #Function to split the string from 2 given values (If you put in 1 and 4 for the word Chicken it'll give "hic")
    try: #Just here to make sure you get what you want
        Val1, Val2 = int(input("\nPut in the first number: ")), int(input("\nPut in the second number: ")) #Gets user input
    except ValueError:
        print("\nTry again")
    else:
        print(stringVal[Val1 : Val2]) #Splits it
        print("Done!")
        return
def StringUpdate(stringVal): #This will change whatever word you want in a string to whatever. 
    print("\nChoose an option") 
    print("\n1. Find the String") #Example: This is a game > change a to not a < This is not a game
    print("\n2. Specific Substring") #Same as the split part, but it puts in the word you want
    optionChosenSub = input("\n> ") #User input
    while True: 
        if optionChosenSub == '1':
           splittedWords = [] 
           splittedWords = stringVal.split(" ") #Converts the sentence or word you put in into a list.
           print(splittedWords, " These are the words available")
           print("\nWhat do you want to find and what do you want it to be changed to?")
           wordToFind = input("\nFind> ") #Input
           wordToChoose = input("\nChoose> ") #Input
           if wordToFind in splittedWords: #This just makes sure that the word you want to change is actually in the list
              splittedWords[splittedWords.index(wordToFind)] = wordToChoose #This changes that word
              print("\nDone!")
              print(" ".join(splittedWords))
              KeepYN = input("\nDo you want to save changes? (y/n)> ") 
              if KeepYN == 'y':
                stringVal = " ".join(splittedWords) 
                return stringVal
              else:
                return
        elif optionChosen == '2':
            while True:
                try: #This just makes sure the program gets what it wants
                    Val1, Val2, StringInput = int(input("\nPut in the first number: ")), int(input("\nPut in the second number: ")), input("And what you want the end to be changed to: ")
                except ValueError:
                    print("\nNuh uh uh, you didn't say the magic word")
                    continue
                else:
                    print("\nHere's your string: ", stringVal[Val1 : Val2] + StringInput) #Changes the word.
                    return
        else:
            print("\nTry again")
            break
def WordFinder(wordToFind):
    if wordToFind in stringVal: #Function to check if a word is in it
        print("\nIt's in here!")
        print("\nWord you wanted to find '{}', and the string you sent in '{}'".format(wordToFind, stringVal))
        return
    else:
        print("\nSorry, nope. Word you wanted to find '{}', the string you sent in '{}'".format(wordOrLetterToFind, stringVal))
        return
def StringLength(stringToMeasure):
    print("The length of the string is: ", len(stringToMeasure)) #Tells you the length of the string
    return
def ConvertAscii(stringToConvert):
    TextArray = []
    TextArray = list(stringToConvert)
    AsciiText = [ord(characters) for Letters in TextArray for characters in Letters] #pulls the letters from the array, then puts each chacter through ord to convert it into ascii
    print(AsciiText)
    return
while True:
    if stringVal != None: #Bunch of options
        print("\nCurrent string: {}".format(stringVal))
        print("\nChoose an option that you want to use")
        print("\n 1. String Splitter")
        print("\n 2. String Update")
        print("\n 3. Word/Letter finder")
        print("\n 4. String Length")
        print("\n 5. Convert to Ascii")
        print("\n 6. Change string")
        print("\n 7. Exit")
        while True:
            optionChosen = input("\n> ")
            if optionChosen == '1':
                StringSplitter()
                break
            elif optionChosen == '2':
                stringVal = StringUpdate(stringVal)
                break
            elif optionChosen == '3':
                userOption = input("\nPut in what you want to find> ")
                WordFinder(userOption)
                break
            elif optionChosen == '4':
                StringLength(stringVal)
                break
            elif optionChosen == '5':
                ConvertAscii(stringVal)
                break
            elif optionChosen == '6':
                stringVal = input("What do you want it changed to?> ")
                stringVal = str.capitalize(stringVal) #This simply changes your previous string
                break
            elif optionChosen == '7':
                sys.exit()
    else:
        print("\nTry that again.")
