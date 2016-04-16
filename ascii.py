from SimpleGraphics import *

def main():
	image = getUserInput()
	asciiNumber = convertToAscii(image)
	printArt(asciiNumber)


def getUserInput():
	#This function loads the image and returns the loaded image file
	imgName = input("Please enter the name of the file : ")
	img = loadImage(imgName)

	return img

def convertToAscii(image):

	#Initalize the a 2d list of values containing 0's
	pixel = [[0 for x in range(getHeight(image)) ] for x in range(getWidth(image))]

	print(len(pixel[0]))
	print(len(pixel))

	#TO BE DELETED LATER
	#Create an image to hold the grayscale version of the image
	imageAltered = createImage(getWidth(image), getHeight(image))

	print( getWidth(image), getHeight(image))
	#Loop through the x and y values of the original picture
	for x in range(0, getWidth(image)):
		for y in range(0, getHeight(image)):

			#Get the RGB Value for that pixel
			r, g, b = getPixel(image, x, y)

			#Find the grayscale value for that pixel
			avg = (r + g + b) // 3


			#Place that grayscale value in the 2d list
			pixel[x][y] = avg


			#TO BE DELETED
			#Add that pixel to the grayscale copy
			putPixel(imageAltered, x, y, avg, avg, avg)

	#TO BE DELETED
	#Draw the grayscale image
	drawImage(imageAltered, 0,0)

	#Return the 2d array of grayscale values
	return pixel


def printArt(array):


	#Find the row
	for y in range(0, len(array) ):

		#Initalize the printed line to nothing 
		charLine = ""

		#Loop through the row and add the character depending on the grayscale value
		for x in range(0, len(array[0])):

			if array[x][y] <= 50:
				charLine +="."
			if array[x][y] > 50 and array[x][y] < 100:
				charLine +=":"
			if array[x][y] > 100 and array[x][y] < 150:
				charLine +="="
			if array[x][y] > 150 and array[x][y] < 200:
				charLine +="?"
			if array[x][y] > 200 and array[x][y] < 255:
				charLine +="@"

		#Print out that line and move onto the new one 
		print (charLine)

main()