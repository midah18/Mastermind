import random

def create_code():
    """
    Random 4 digit code is initalized
    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code

 
def get_user_imput(code):
    """
    making sure that the code is 4 digits long
    comparing values and position
    """

    turns = 0
    while turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        
        if correct_digits_and_position == 4:
            correct = True
            print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
            print('Number of correct digits not in correct place: '+str(correct_digits_only))
            print('Congratulations! You are a codebreaker!')
            print('The code was: '+str(code))
            return
        else:
            print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
            print('Number of correct digits not in correct place: '+str(correct_digits_only))
            turns += 1
            print('Turns left: ' +str(12 - turns))
    print('The code was: '+str(code))
        

def run_game():
    """
    The code starts here
    """
    code = create_code()
    get_user_imput(code)
    
if __name__ == "__main__":
    run_game()