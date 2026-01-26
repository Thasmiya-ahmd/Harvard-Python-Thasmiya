months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while(True):
        date = input("Date:").strip()

        if "/" in date:
            temp = date.split("/")
            month,date,year=temp
            if not month.isdigit() or not date.isdigit() or  not year.isdigit():
                continue
            month=int(month)
            date=int(date)
            year=int(year)
            if month>=1 and month<=12 and date>=1 and date<=31:
                print(f"{year}-{month:02}-{date:02}")
            break
    
        try:
            temp = date.split(" ")
            month,temp=temp
        except ValueError:
            continue
        if month in months:
            list = temp.split(",")
            date,year=list
            month = months.index(month) + 1
            date=int(date)
            year=int(year)
            if month>=1 and month<=12 and date>=1 and date<=31:
                print(f"{year}-{month:02}-{date:02}")
            break

main()
