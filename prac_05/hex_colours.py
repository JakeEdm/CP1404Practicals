"""Hex Colours"""

COLOUR_TO_HEX = {"blueviolet": "#8a2be2", "chocolate": "#d2691e", "green": "#00ff00", "hotpink": "#ff69b4",
                 "light": "#eedd82", "lightsalmon": "#ffa07a", "medium": "#66cdaa", "navyblue": "#000080",
                 "pale": "#db7093", "red": "#ff0000"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(f'{colour} is {COLOUR_TO_HEX[colour]}')
    else:
        print("Invalid choice")
    colour = input("Enter a colour: ").lower()


