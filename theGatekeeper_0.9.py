import time 
from PIL import Image

currentTime = int(time.time())

generatedNumber = (currentTime % 100) + 50 

if generatedNumber % 2 == 0:
    generatedNumber += 10 

print('Current time = ' + str(currentTime))
print(generatedNumber)

im = Image.open("F:/UNI/HIT137/Assignment2/chapter1.jpg")

oData = im.getdata()

newPixels = []

for r, g, b in oData:
    nRed = r + generatedNumber
    nGreen = g + generatedNumber
    nBlue = b + generatedNumber
    nData = (nRed, nGreen, nBlue)
    newPixels.append(nData)

newImage = Image.new(im.mode, im.size)
newImage.putdata(newPixels)
newImage.save("F:/UNI/HIT137/Assignment2/TEST" + str(time.time()) + ".jpg")
newImage.show()




