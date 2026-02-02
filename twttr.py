def main():
    words=input("Input ")
    words=shorten(words)
    print(f"Output: {words}")

def shorten(words):
    text=""
    for ch in words:
        if ch not in ["a","e","i","o","u","A","E","I","O","U"]:
            text+=ch
    words=text
    return words

if __name__=="__main__":
    main()