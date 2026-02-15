from datetime import date,datetime
import sys
import inflect

def main():
    p=inflect.engine()
    dat=input("Date of Birth: ").strip()
    if not "-" in dat:
        sys.exit("Invalid date")
    d2=date.today()
    d1=datetime.strptime(dat,'%Y-%m-%d').date()
    diff=abs(d1-d2).days
    minutes=diff*24*60
    word=p.number_to_words(minutes,andword="")
    print(f"{word} minutes")

if __name__=="__main__":
    main()
