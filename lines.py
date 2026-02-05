import sys

def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too Many command-line arguments")
    if not sys.argv[1].endswith('.py'):
        sys.exit("NOt a python file")
    files=sys.argv[1]
    x=0
    try:
        with open(files,"r") as f:
            for file in f:
                file=file.lstrip()
                if file=="" or file.startswith('#'):
                    continue
                x+=1
        print(x)
    except FileNotFoundError:
        sys.exit("File doesnot exist")

  
if __name__=="__main__":
    main()