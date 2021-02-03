import random

def run_game():
    """
    4 digit code is initialized
    """
    number = [0, 0, 0, 0]
    i = 0
    while i < len(number):
        x = random.randint(1, 8)
        if x in number:
            continue
        number[i] = x
        i += 1
    number = list(map(str,number))
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    """
    if  the length of the code is not equal to 0 and
    is not equal to 4 , ask again.
    if 0 and 9 in the user input, stop running
    """
    attempts = 12
    while attempts != 0:
        num  = input("Input 4 digit code: ")

        while len(num) != 4:
            print("Please enter exactly 4 digits.")
            num  = input("Input 4 digit code: ")
        num_num = list(num)
        if '0' in num_num or '9' in num_num:
                return 

        a = 0
        b = 0
        lsnumber = number #4 digit code
        lsnum = num #user code

        """
        if position i (random code) and position x (user code)
        are equal, increment.
        else if position x in lsnumber and i not in x, increment;
        basically number is present but not in the correct place
        """ 
        for i, x in zip(lsnumber, lsnum):
            if i == x:
                a += 1
            elif x in lsnumber and i != x:
                b += 1
        print("Number of correct digits in correct place:     " +str (a))
        print("Number of correct digits not in correct place: " +str (b))

        if a == 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: " +str("".join(number)))
            break
        attempts -= 1
        print("Turns left: " +str(attempts))
    
if __name__ == "__main__":
    run_game()