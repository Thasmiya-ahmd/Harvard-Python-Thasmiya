import csv
import sys

def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too Many command-line arguments")
    if not sys.argv[1].endswith('.csv') and not sys.argv[2].endswith('.csv'):
        sys.exit("NOt a CSV file")
    filename=sys.argv[1]
    output=sys.argv[2]
    try:
       with open(filename,"r") as f,open(output,"w",newline="") as out:
           content=csv.DictReader(f)
           writer=csv.DictWriter(out,fieldnames=["first","last","house"])
           writer.writeheader()
           for row in content:
               name_list=row["name"].split(",")
               writer.writerow(
                   {
                       "first":name_list[0],
                       "last":name_list[1].strip(),
                       "house":row["house"]
                   }
                )
    except FileNotFoundError:
        sys.exit("File doesnot exist")

  
if __name__=="__main__":
    main()
