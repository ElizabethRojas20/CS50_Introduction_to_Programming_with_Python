from pyfiglet import Figlet
import sys
import random #to choose a random font when no especified

#create what will generate the ASCII text
figlet = Figlet()

#list of available fonts
fonts = figlet.getFonts()

#only one item -> random
if len(sys.argv) == 1:
    font = random.choice(fonts)

#including -f or --font
elif len(sys.argv) == 3:
    #we check the "-f" or "--font"
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        #we check our library
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

#we put the chosen font
figlet.setFont(font=font)

#input
textin = str(input("Input: "))
print("Output:", figlet.renderText(textin))