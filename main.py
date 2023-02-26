from PIL import Image, ImageOps

imgData = open("imgData","w")

i = Image.open("./images/4.1.01.png")
g = ImageOps.grayscale(i)
#g.save("testImg.png")
pix = g.load()

for i in range(50):
    for j in range(50): 
        imgData.write("("+str(pix[i,j])+")")

    imgData.write("\n")