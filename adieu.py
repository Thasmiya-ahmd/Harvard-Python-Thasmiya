import inflect

def main():
    p=inflect.engine()
    names=[]
    try:
        while(True):
            text=input("Name: ")
            names.append(text)
    except KeyboardInterrupt:
        print()
    if len(names)==1:
        names=p.join(names,conj='')
    else:
        names=p.join(names,sep=',',sep_spaced=False)
        names=names.replace(", and ",",and ")
    print(f"Adieu,adieu,to {names}")
    
     
main()