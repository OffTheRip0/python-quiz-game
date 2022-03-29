#importing what is needed and welcoming the user
from multiprocessing.connection import wait
import random
import time
print("Please enter your name")
name = input("> ")
print("Hello " + name + " Welcome to a quiz about New Zealand.")
score = 0

#class for colours to use in print
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#wip
q = ["Is Zealandia a bird sanctuary?", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
q_done = []

#the main function that asks the question and checks the users input and gives and output based on that
def question(question, ans, choices):
    global score
    print(f"{colors.OKCYAN}" + question)
    print(f"{colors.ENDC}{colors.ENDC}")
    print(choices)
    print("---------------")
    print("Enter Your Choice [a/b/c/d]")
    choice = input("> ")
    #loop for the questions
    while(True):
        #wrong choice option
        if choice.lower() in ['a', 'b', 'c', 'd'] and choice.lower() != ans:
            pass
            print(f"{colors.FAIL}Wrong{colors.ENDC}")
            print("---------------")
            break
        #correct choice option
        elif choice.lower() == ans:
            print(f"{colors.OKGREEN}Great You've Got It!{colors.ENDC}")
            print("---------------")
            score = score + 1
            break
        #invalid input option
        else:
            print(f"{colors.WARNING}Invalid choice enter again.{colors.ENDC}")
            print(f"{colors.OKCYAN}" + question)
            print(f"{colors.ENDC}{colors.ENDC}")
            print(choices)
            print("---------------")
            print("Enter Your Choice [a/b/c/d]")
            choice = input("> ")

#calling the main function (question) and giving it the arguments it needs
question("Is Zealandia a bird sanctuary?", "a", "A = Yes  | B = No | C = Maybe | D = IDK")

question("What animal can you find on a 1 dollar coin?", "b", "A = Kakapo  | B = Kiwi | C = Pigeon | D = Seal")

question("How many official languages are there in NZ?", "c", "A = 4  | B = 3 | C = 2 | D = 1")

question("What is a Tuatara?", "b", "A = Mammal  | B = Reptile | C = Bird | D = Insect")

question("What is the largest lake in New Zealand?", "d", "A = Lake Benmore  | B = Lake Rotorua | C = Lake Tekapo | D = Lake Taupo")

question("What is the largest city in New Zealand?", "c", "A = Queenstown  | B = Wellington | C = Auckland | D = Christchurch")

question("What is the largest glacier in New Zealand?", "a", "A = Tasman Glacier  | B = Fox Glacier | C = Ramsay Glacier | D = Franz Josef Glacier")

question("In which city can you find the Sky Tower?", "b", "A = Queenstown  | B = Auckland | C = Wellington | D = Christchurch")

question("When did New Zealand gain independence from Britain?", "c", "A = 1420  | B = 1969 | C = 1947 | D = 1948")

question("What is the name of the national rugby team?", "a", "A = All Blacks  | B = Black Cocks | C = hmmm | D = IDK")

#finishing the game and telling the user the score
print("---------------")
def calculate_score():
    global score
    #if score is 10 say smth nice
    if score == 10:
        print("Great!, You got all of them!")
    #if its 0 say smth dissapointing
    elif score == 0:
        print("srsly?? 0?")
        #if its anything else say the score
    else:
        print("You got " + str(score) + " questions correct.")

#run calculate_score function
calculate_score()
print("---------------")
print("Thanks for playing!")
print("Window will close in 30 secs")
time.sleep(30)


