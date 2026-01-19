def main():
    grocery={}
    while(True):
        try:
            item=input("")
            if item in grocery:
                grocery[item]+=1
            else:
                grocery[item]=1
        except KeyboardInterrupt:
            print("")
            break
    sortd=dict(sorted(grocery.items()))
    for item in sortd:
        print(f"{grocery[item]} {item.upper()}")

main()
    