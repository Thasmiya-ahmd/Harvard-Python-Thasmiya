def main():
    while True:
        try:
            fraction=input("Fraction:").strip()
            f=fuel(fraction)
            if f=="E" or f=="F":
                print(f"{f}")
            else:
                print(f"{f}%")
            break
        except (ValueError,ZeroDivisionError):
            pass

def fuel(fraction):
    X,Y=fraction.split("/")
    if not X.isdigit() or not Y.isdigit() or int(X)>int(Y):
        raise ValueError()
    if Y==0:
        raise ZeroDivisionError()
    X=int(X)
    Y=int(Y)
    fraction=round((X/Y)*100)
    if fraction<=1:
        return "E"
    if fraction>=99:
        return "F"
    return fraction

main()



