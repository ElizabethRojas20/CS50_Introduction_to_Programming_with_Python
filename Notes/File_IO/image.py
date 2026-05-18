from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("hello.jpg") as img:
        print(img.size)
        print(img.format)
        img.rotate(180).save("goodbye.jpg")

        img.filter(ImageFilter.FIND_EDGES).save("edges.jpg")
        img.filter(ImageFilter.BLUR).save("blur.jpg")

main()