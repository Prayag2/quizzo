# IMPORT
import os, sys, ast
from termcolor import colored
from time import sleep
from random import shuffle, randint

# VARIABLES
score = 0
rnd = 1

# FUNCTIONS
def t_print(text, color='yellow', end='\n'):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.write(end)
def c_print(text, color='yellow'):
    print(colored(text, color))

# MAIN
def main():

    # DATA
    data = {
        'money': 0,
        'question': 1,
        'hints_left': 2
    }
    # CLEAR
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # CHECK ANS
    def check_ans(ans, options):
        global score, rnd
        clear()
        if ans == options[0]:
            score+=1
            c_print(r'''   ___ ___  ___ ___ ___ ___ _____ _ _ 
  / __/ _ \| _ \ _ \ __/ __|_   _| | |
 | (_| (_) |   /   / _| (__  | | |_|_|
  \___\___/|_|_\_|_\___\___| |_| (_|_)
                                      ''', 'green')
        else:
            c_print(r''' __      _____  ___  _  _  ___ _ _ 
 \ \    / / _ \/ _ \| \| |/ __| | |
  \ \/\/ /|   / (_) | .` | (_ |_|_|
   \_/\_/ |_|_\\___/|_|\_|\___(_|_)
                                   ''', 'red')
        if rnd == 10:
            c_print(f"COMPLETE! YOU ANSWERED {score} OUT OF 10 QUESTIONS CORRECTLY!")
            sleep(5)
            exit()
        rnd+=1
        sleep(1)

    # DRAW LAYOUT
    def draw_l(question, score, round, options):
        clear()
        if len(question) > 60:
            dashes = '-'*90
        else:
            dashes = '-'*(len(question) + 2)
            q_dashes = '-'*int(((len(question)-8)/2) + 1)
            q = '| ' + question.upper() + ' |'
        c_print(f'{"+--SCORE--+":<50}{"+--ROUND--+":>50}', 'blue')
        c_print(f'{f"{score:^11}":>11}{f"{round:^11}":>89}', 'blue')
        c_print(f'{"+---------+":<50}{"+---------+":>50}', 'blue')
        c_print(f'{f"+{q_dashes}QUESTION{q_dashes}+":^100}', 'red')
        c_print(f'{q:^100}', 'red')
        c_print(f'{f"+{dashes}+":^100}', 'red')

        # options
        new_options = []
        for item in options:
            new_options.insert(randint(0, 4), item)

        for option in new_options:
            o_dashes = '-'*(len(option) + 6)
            o = '| ' + option.upper() + ' |'
            o_no = str(new_options.index(option) + 1)
            c_print(f'{f"+{o_dashes}+":^100}', 'yellow')
            c_print(f'{"| " + o_no + " " + o:^100}', 'yellow')
            c_print(f'{f"+{o_dashes}+":^100}', 'yellow')
        
        print(f"\n{'ENTER 1, 2, 3 OR 4':^100}")
        while True:
            ans_i = int(input(f"{'=>':>50}"))
            if ans_i > 4 or ans_i < 1:
                c_print("OUT OF RANGE", 'red')
            elif type(ans_i) != int:
                c_print("ENTER A NUMBER")
            else:
                ans = new_options[ans_i - 1]
                check_ans(ans, options)
                break

    # CHECK QUESTIONS
    def check_questions():
        with open('questions.txt') as x:
            dt = x.read()
            questions = ast.literal_eval(dt)
        shuffle(questions)
        for question in questions:
            draw_l(question['question'], score, rnd, question['options'])

    # INTRO
    def intro():
        t_print("Welcome to quizzo! You have to answer some questions. If you answer a question correctly, you will score 1 point! There are 10 questions in this game. Let's begin!")
        sleep(4)
        check_questions()
    
    # CLEAR THE CONSOLE IN THE BEGINNING
    clear()
    intro()

# CALLING MAIN
if __name__ == "__main__":
    main()