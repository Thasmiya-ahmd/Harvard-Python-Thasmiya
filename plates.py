def main():
    plate=input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (len(s)<=6 and len(s)>=2):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    for ch in s:
        if not ch.isalnum():
            return False  
  
    for i in range(0,len(s)):
        if s[i].isdigit() :
            if  s[i] == "0":
                return False 
            for j in range(i+1,len(s)):
                if s[j].isalpha():
                    return False
            return True
    return True


if __name__=="__main__":
    main()