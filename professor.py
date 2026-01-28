import random

def main():
    level=get_level()
    total=0
    t=0
    while t<10:
        r=0
        x,y=generate_integer(level)
        z=x+y
        while r<3:
            try:
                w=int(input(f"{x} + {y} = "))
                if w==z:
                    total+=1
                    break
                else:
                    print("EEE")
                    r+=1
                    continue
            except ValueError:
                print("EEE")
                r+=1
                continue
        if r==3:
            print(f"{x}+{y}={z}")
        t+=1
    print(f"Score={total}")


def get_level():
    while (True):
       try:
            level=int(input("Level: "))
            if level not in [1,2,3]:
                continue
       except ValueError:
           continue
       return level


def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    x,y=random.randint(10**(level-1),10**level-1),random.randint(10**(level-1),10**level-1)
    return x,y
    

if __name__=="__main__":
    main()