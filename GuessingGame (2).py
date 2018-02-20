import random #Import needed modules.
import time
while True:
	computerGuessMinimum, computerGuess, numGuesses = 1, 1, 0 #Hard coded values
	word_List = ["\n Im gonna guess it's {}", "\n Is it this? {}?", #Word list for computer to say.
			 "\n The magic crystal ball is telling me your secrets.... is this your number? {}",
			 "\n I'm calling all of the worlds experts to guess this one. After years of analysis, we came to the conclusion that this is your number {}",
			 "\n Im just spitting out numbers here, but is it {}?", "\n Lets go again, how about this {}?", "\n Oh heck. Hmm.. This? {}",
			 "\n The voices are telling me its {}", "\n What about this? {}", "\n My spidy senses are tingling, is it {}", "\n Easy, its {}.... wait is it?",
			 "\n It's obviously {}.. right?", "\n The memes point to this {}", "\n This just in, the number is {}.. i think.", "\n Well judging from past choices, i think it's {}",
			 "\n Pfffft. Easy. {}", "\n I'm gonna take a wild guess and say its this {}", "\n If you really think about it, it's obviously this {}", "\n Going out on a limb here, is it {}?",
			 "\n The ancients are telling me its {}"]
		
	while True: #Checking user input
		try:
			computerGuessMax, userInput = int(input('\n Please put in a maximum value for the game! ')), int(input("\n Pick a number "))
		except ValueError:
			print("\n Put in a number please \n")
			continue
		else:
			if computerGuessMax < userInput:
				print("\n Please put in either a bigger maximum number or a smaller choice. \n")
			else:
				break
				
	while computerGuess != userInput: #Does the calculations
		computerGuess = random.randint(computerGuessMinimum, computerGuessMax - 1)
		print(random.choice(word_List).format(computerGuess));
		numGuesses += 1
		time.sleep(2)	
		if computerGuess > userInput:
			computerGuessMax = computerGuess		
		elif computerGuess < userInput: 
			computerGuessMinimum = computerGuess + 1	
			
	print('\n I got it right! Its {}! it took me {} guesses!'.format(computerGuess, numGuesses)) #Prints out the computers guess
																					   		     #and how many times it took to get it
	while True: #Asks if the user wants to play again and checks it input
		YesNo = input('\n Run again? (y/N): ')
		if YesNo in ('y', 'n', ''):
			break
		print('\n y or n please')
	if YesNo == 'y': #Checks if it's Y
		continue
	break #Gets out of the code if it isn't
