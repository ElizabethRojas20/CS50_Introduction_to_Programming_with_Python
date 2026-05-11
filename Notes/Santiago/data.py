xy = []
xz = []

with open("ab42_nk2.txt", "r") as file:
    for line in file:
        x, y, z = line.strip().split("\t")
        z = z.replace("E", "*^")

        xy.append(f"{{{x}, {y}}}")
        xz.append(f"{{{x}, {z}}}")

re_xy = "{" + ", ".join(xy) + "}"

re_xz = "{" + ", ".join(xz) + "}"


with open("ab42_nk2_new.txt", "w") as download:
    download.write("xy = " + re_xy + "\n\n")
    download.write("xz = " + re_xz)