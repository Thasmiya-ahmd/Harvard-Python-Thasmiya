def main():
    greeting=input("greeting: ").strip().lower()
    print(value(greeting))

def value(greeting):
    new=greeting.split(" ")
    if new[0]=="hello":
        return "$0"
    elif greeting[0]=="h":
        return "$20"
    else:
        return "$100"

if __name__=="__main__":
    main()