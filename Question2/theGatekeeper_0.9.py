import time 
from PIL import Image

currentTime = int(time.time())

generatedNumber = (currentTime % 100) + 50 

if generatedNumber % 2 == 0:
    generatedNumber += 10 

print('Current time = ' + str(currentTime))

#.open loads the image. getdata retrieves the data from the loaded image and stores it in list "oData"
im = Image.open("F:/UNI/HIT137/Assignment2/chapter1.jpg")
oData = im.getdata()

#Define a new list that will be populated with the new pixel data
newPixels = []

#Iterate through every pixel in oData, adding the generated number to each respective element. Then append to newPixels. 
for r, g, b in oData:
    nRed = r + generatedNumber
    nGreen = g + generatedNumber
    nBlue = b + generatedNumber
    nData = (nRed, nGreen, nBlue)
    newPixels.append(nData)


#Create a new image with the same mode and size as the original. Mode is how the pixel values are stored, such as RGB. putdata does what it says on the tin. Then save and show it to the user. 
newImage = Image.new(im.mode, im.size)
newImage.putdata(newPixels)
newImage.save("F:/UNI/HIT137/Assignment2/TEST" + str(time.time()) + ".jpg") #Change name from test 
newImage.show()

#This next block takes all the red values of the new image and adds them, as per the assignment requirement. Print needs to be removed from this block in future to clean it up. 
totalRed = 0
for nRed, nGreen, nBlue in newPixels:
    totalRed = totalRed + nRed
print(totalRed) #Remove 




 
