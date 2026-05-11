def main():
    time = (str(input("What time is it? "))).strip()
    timef = convert(time)

    if time.startswith("12") and time.endswith("a.m."):
        print("")

    elif (time.startswith("12") and time.endswith("p.m.")) or time == "13:00":
        print("lunch time")

    elif timef >= 7 and timef <=8:
        print("breakfast time")

    elif timef >= 12 and timef <=13:
        print("lunch time")

    elif timef >= 18 and timef <=19:
        print("dinner time")

    else:
        print("")

def convert(time):

    if time.endswith("a.m."):
        time = time.replace(" a.m.", "")
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)/60
        timef = hours + minutes
        return timef

    elif time.endswith("p.m."):
        time = time.replace(" p.m.", "")
        hours, minutes = time.split(":")
        hours = int(hours) + 12
        minutes = int(minutes)/60
        timef = hours + minutes
        return timef

    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)/60
        timef = hours + minutes
        return timef


if __name__ == "__main__":
    main()