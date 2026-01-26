from pyfiglet import Figlet
import sys


def main():
    figlet = Figlet()
    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("invalid flag")
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("invalid usage")
        figlet.setFont(font=sys.argv[2])
    elif len(sys.argv) != 1:
        sys.exit("invalid usage")
    
    text = input("Input:")
    print(figlet.renderText(text))


main()
