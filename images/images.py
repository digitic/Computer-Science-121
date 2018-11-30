import imagetools
import copy


##### Generating images

def rainbow():
    image = []
    horiz = 0
    while(horiz < 256):
        line = []
        vert = 0
        while(vert < 256):
            line.append([horiz, vert, 128])
            vert += 1
        image.append(copy.deepcopy(line))
        horiz += 1
    return image


def formula_art():
    image = []
    horiz = 0
    while(horiz < 1000):
        line = []
        vert = 0
        while(vert < 1000):
            line.append([(horiz % (vert+1) % 256), (vert % (horiz+1) % 256), 128])
            vert += 1
        image.append(copy.deepcopy(line))
        horiz += 1
    return image

def my_formulaic():
    image = []
    modifier = [4, 2, 7, 1, 9, 0, 3, 6, 8, 5]
    horiz = 0
    while(horiz < 600):
        line = []
        vert = 0
        while(vert < 600):
            line.append([(horiz * (modifier[vert % 10]) % 256), ((vert - (modifier[horiz % 10])) % 256), 128])
            vert += 1
        image.append(copy.deepcopy(line))
        horiz += 1
    return image

##### Manipulating images


def width(array):
    return len(array[0])

def height(array):
    return len(array)

def grayscale(pic):
    image = []
    horiz = 0
    while(height(pic) > horiz):
        vert = 0
        row = pic[horiz]
        line = []
        while(width(pic) > vert):
            #print(vert)
            pix = row[vert]
            avg = (pix[0] + pix[1] + pix[2]) // 3
            line.append([avg, avg, avg])
            vert += 1
        image.append(copy.deepcopy(line))
        horiz += 1
    return image

def leave_purple(pic):
    image = []
    horiz = 0
    while(height(pic) > horiz):
        vert = 0
        row = pic[horiz]
        line = []
        while(width(pic) > vert):
            pix = row[vert]
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if(red <= green or blue <= green):
                avg = (red + green + blue) // 3
                line.append([avg, avg, avg])
            else:
                line.append([red, green, blue])
            vert += 1
        image.append(copy.deepcopy(line))
        horiz += 1
    return image

def crop(pic, left, top, right, bottom):
    image = []
    length = len(pic)
    i = left
    while(i < (length - right)):
        row = copy.deepcopy(pic[i])
        rowLen = len(row)
        rowShort = row[bottom:(rowLen - top)]
        image.append(copy.deepcopy(rowShort))
        i += 1
    return image

def enlarge(pic, factor):
    image = []
    row = 0
    while(row < height(pic)):
        factRow = 0
        while(factRow < factor):
            col = 0
            line = []
            while(col < width(pic)):
                factCol = 0
                while (factCol < factor):
                    line.append(pic[row][col])
                    factCol += 1
                col += 1
            image.append(copy.deepcopy(line))
            factRow += 1
        row += 1
    return image




def distance(x, y, x2, y2):
    dist = (((y2 - y)**2) + ((x2 - x)**2))**0.5
    return dist

def blur(pic, radius):  
    image = []
    for y in range(len(pic)):
        row = []
        for x in range(len(pic[y])):
            xMin = max(0, x - radius)
            yMin = max(0, y - radius)
            yMax = min(y + radius, len(pic))
            xMax = min(x + radius, len(pic[y]))
            r = 0
            g = 0
            b = 0
            z = 0
            for a in range(yMin, yMax):
                for b in range(xMin, xMax):
                    if(distance(b, a, x, y) <= radius):
                        r += pic[a][b][0]
                        g += pic[a][b][1]
                        b += pic[a][b][2]
                        z += 1
            r = r // z
            g = g // z
            b = b // z
            row.append([r, g, b])
        image.append(copy.deepcopy(row))
    return image

                        


def my_effect(pic):
#This code is meant to create an inverse color scheme, like a negative.
    #Creating blank image and row counter
    image = []
    horiz = 0
    #While loop, every row
    while(height(pic) > horiz):
        #Set / Reset my column counter, line to store data, and make row = pic's row
        vert = 0
        row = pic[horiz]
        line = []
        #While loop, every column
        while(width(pic) > vert):
            #Set pix to the individual pixel I want to look at
            pix = row[vert]
            #Invert the color for each RGB value
            line.append([255 - pix[0], 255 - pix[1], 255 - pix[2]])
            #Increment column
            vert += 1
        #Copy the line into the end of the image
        image.append(copy.deepcopy(line))
        #increment row
        horiz += 1
    #Return the new image
    return image

