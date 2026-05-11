felipe = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

TOTAL = 0

while True:
    try:
        menu = str(input("Item: ")).lower().strip()
        if menu in felipe:
            item = float(felipe[menu])
            TOTAL += item
            print(f"${TOTAL:.2f}")

    except EOFError:
        break