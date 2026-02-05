import sys
from tabulate import tabulate
import csv 

def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too Many command-line arguments")
    if not sys.argv[1].endswith('.csv'):
        sys.exit("NOt a CSV file")
    filename=sys.argv[1]
    try:
        with open(filename,"r") as f:
            content=csv.reader(f)
            table=[]
            head=[]
            i=1
            for row in content:
                if i==1:
                    head=row
                    i=0
                    continue
                table.append(row)
            print(tabulate(table,headers=head,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File doesnot exist")

  
if __name__=="__main__":
    main()