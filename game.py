import random

def main():
    num=random.randrange(1,100,1)
    while(True):
        try:
            level=int(input("Level: "))
            if level<0:
                continue
            break
        except ValueError:
            continue
    while(True):
        try:
            guess=int(input("Guess: "))
        except ValueError:
            continue
        if guess<0:
            continue
        elif guess==num:
            print("Just right!!")
            break
        elif guess<num:
            print("Too Small!!")
            continue
        else:
            print("Too Large!!")
            continue


main()