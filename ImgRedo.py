import json, pandas, numpy, PIL, sys, os
from pandas.io.json import json_normalize
from PIL import Image, ImageDraw

global sheet # Define the object sheet as global, so the function can write on it and store even after the function closes
global wdth
global hgth

def Neo(jsf):
	
	global wdth
	global hgth
	global sheet
	
	data = json.load(open(jsf)) # Load the json file as a dict

	df = json_normalize(data, 'views').assign(**data) # Normalize the json object wich allow retriving the coordinates as a list.
	
	# Define the width and height of the image based on the information in the json.
	wdth = df.width[0]
	hgth = df.height[0]

	ee = df.coords[0] #List of coordinates of the image as a list of strings. Each piece of the image is represented as a string with the x,y coordinate of the upper left corner, a sum to obtain the right lower corner and lastly the original left upper corner that the piece should go.
	
	for e in range(0,len(ee)): # Remove the first part of every string in the list (the 'i:' part) resulting in a list of string only with the coordinates and function.
		clean = ee[e].split('i:')
		ee[e] = clean[1]
	
	sheet = numpy.zeros((len(ee),8)) # Create the matrix that going to store each X and Y value of the pieces of the image.

	for i in range(0,len(ee)): # for loop used to split each string of the list as the subsequent individual coordinates, convert the string in integer, do the math required to get all coordinates and at last write in the matrix the values.
		coor = ee[i] # Getting the string correspondet to the piece of image being manipulated in the interaction 'i' from the loop
		co1 = coor.split('+') # Spliting the upper left coordinate from the rest, this object is a list with 2 strings
		co2 = co1[1].split('>') # Spliting the values used in the sum from the REAL upper left coordinates the piece of image should go
		co1 = co1[0] # Making this object hold only the string from the upper left coordinate
		co3 = co2[1] # Making this object hold only the string from the REAL coordinate
		co2 = co2[0] # Making this object hold only the string with the values to be used in the sum
		
		co1 = co1.split(',') # Spliting the string into two, the coordinate X and Y
		co2 = co2.split(',') # Spliting the string into two, the values to be summed with coordinate X and Y
		co3 = co3.split(',') # Spliting the string into two, the coordinate X and Y
		
		# Converting the string into integer and writing in the matrix
		sheet[i,0] = int(co1[0])
		sheet[i,1] = int(co1[1])
		sheet[i,2] = int(co2[0])
		sheet[i,3] = int(co2[1])
		sheet[i,4] = int(co1[0])+int(co2[0]) # Writing and making the sum to know the lower right corner from the piece of image
		sheet[i,5] = int(co1[1])+int(co2[1])
		sheet[i,6] = int(co3[0])
		sheet[i,7] = int(co3[1])


def DrFrank(img,DirPath):
	
	im = Image.open(img)
	rdy = Image.new('RGBA',(wdth,hgth),'White')
	for r in range(0,sheet.shape[0]):
		name = os.path.splitext(img)[0]
		cpy = im.crop([sheet[r,0],sheet[r,1],sheet[r,4],sheet[r,5]])
		rdy.paste(cpy,([int(sheet[r,6]),int(sheet[r,7])]))
	rdy.save(DirPath+'/'+name+'_new'+'.png',format='png')
	print(img+': Done')


def Surgery():
	lista = []
	lista = os.listdir(DirPath) # Lista de todos os arquivos dentro da pasta
	lista = sorted(lista)
	JsFile = []
	fotos = [] # Este script so executa se uma pasta for escolhida. A primeira coisa a ser feita e limpar a lista de imagens. 

	for files in lista:
		arq = os.path.splitext(files)[-1]
		if arq == '.png' or arq == '.jpg' or arq == '.jpeg' or arq == '.PNG' or arq == 'JPG' or arq == 'JPEG':
			fotos.append(files)
		elif arq == '.json' or arq == '.Json' or arq == '.JSON':
			JsFile.append(files)
		
	for item in range(0,len(JsFile)):
		jsf = JsFile[item]
		img = fotos[item]
		Neo(jsf)
		DrFrank(img,DirPath)
	
	
DirPath = raw_input("Enter the directory-> ")
Surgery()