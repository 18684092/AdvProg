from pathlib import Path
import binascii

class bitMapFileHeader():
    imageType = "00"    # 2 bytes
    fileSize = "0000"   # 4 bytes
    reserved1 = "00"    # 2 bytes
    reserved2 = "00"    # 2 bytes
    fileOffset = "0000" # 4 bytes
    fileDescription = ""

class BITMAPINFOHEADER():
    headerSize = "0000"             # 4 bytes
    bitmapWidth = "0000"            # 4 bytes
    bitmapHeight = "0000"           # 4 bytes
    numberOfColourPlanes = "00"     # 2 bytes
    colourDepth = "00"              # 2 bytes
    compressionMethod = "0000"      # 4 bytes
    imageSize = "0000"              # 4 bytes
    horizontalResolution = "0000"   # 4 bytes
    verticalResolution = "0000"     # 4 bytes
    numberColours = "0000"          # 4 bytes
    numberImportantColours = "0000" # 4 bytes

class BMP():

    def __init__(self, filename):
        """ Init file format """
        self.fileName = filename
        self.rawString = self.readFile()
        if not self.rawString == "ERROR":
            self.fileHeader = self.makeFileHeader()
            self.DIBHeaderType = self.determineDIB()
            self.DIBHeader = self.makeDIBHeader()
            self.imageData = self.getImageData()
        else:
            raise ValueError("File Not Found")

    def getImageData(self):
        imageData = []
        # offset is last line of bitmap
        offset = self.fieldToDec(self.fileHeader.fileOffset) 
        x = self.getImageWidth()
        padding= x % 4
        for y in range(self.getImageHeight()-1,0,-1):
            temp = []
            d = offset + (y * ((x  * 3) + padding)) 
            #print(self.getImageHeight(), offset, x , y, d, len(self.rawString))
            for pixel in range(x):
                blue = ord(self.rawString[d])
                green = ord(self.rawString[d + 1])
                red = ord(self.rawString[d + 2])
                temp.append((red, green, blue))
                d += 3
            imageData.append(temp)
        return(imageData)        
            
    def readFile(self):
        """ Read BMP File into string """
        if not Path(self.fileName).is_file():
            return("ERROR")
        f = open(self.fileName, 'rb')
        rawString = bytearray(f.read())
        f.close()
        return(rawString)

    def determineDIB(self):
        t = self.rawString[14:18]
        tSize = self.fieldToDec(t)
        if tSize == 12:
            return("BITMAPCOREHEADER")
        elif tSize == 40:
            return("BITMAPINFOHEADER")
        elif tSize == 64:
            return("OS22XBITMAPHEADER2")
        elif tSize == 16:
            return("OS22XBITMAPHEADER")
        elif tSize == 52:
            return("BITMAPV2INFOHEADER")
        elif tSize == 56:
            return("BITMAPV3INFOHEADER")
        elif tSize == 108:
            return("BITMAPV4INFOHEADER")
        elif tSize == 124:
            return("BITMAPV5INFOHEADER")
        else:
            return("UNKNOWN")

    def makeDIBHeader(self):
        DIBHeader = BITMAPINFOHEADER()
        if self.DIBHeaderType == "BITMAPINFOHEADER":
            DIBHeader.headerSize = self.rawString[14:18]
            DIBHeader.bitmapWidth = self.rawString[18:22]
            DIBHeader.bitmapHeight = self.rawString[22:26]
            DIBHeader.numberOfColourPlanes = self.rawString[26:28]
            DIBHeader.colourDepth = self.rawString[28:30]
            DIBHeader.compressionMethod = self.rawString[30:34]
            DIBHeader.imageSize = self.rawString[34:38]
            DIBHeader.horizontalResolution = self.rawString[38:42]
            DIBHeader.verticalResolution = self.rawString[42:46]
            DIBHeader.numberColours = self.rawString[46:50]
            DIBHeader.numberImportantColours = self.rawString[50:54]
            return(DIBHeader)
        else:
            return(DIBHeader)

    def makeFileHeader(self):
        fileHeader = bitMapFileHeader()
        fileHeader.imageType = self.rawString[0:2]
        it = fileHeader.imageType
        fileHeader.fileSize = self.rawString[2:6]
        fileHeader.reserved1 = self.rawString[6:8]
        fileHeader.reserved1 = self.rawString[8:10]
        fileHeader.fileOffset = self.rawString[10:14]
        t = ""
        if it == "BM":
            t = "Windows"
        elif it == "BA":
            t = "OS/2 struct bitmap array"
        elif it == "CI":
            t = "OS/2 struct colour icon"
        elif it == "CP":
            t = "OS/2 const colour pointer"
        elif it == "IC":
            t = "OS/2 struct icon"
        elif it == "PT":
            t = "OS/2 pointer"
        fileHeader.fileDescription = t
        return(fileHeader)

    def getImageType(self):
        """ Returns BMP file type Windows or OS/2 etc """
        return(self.fileHeader.fileDescription)

    def fieldToDec(self, field):
        """ converts little endian in ASCII to binary to decimal """
        size = ""
        print(field)
        #for d in field[::-1]:
        #    size += format(ord(d), '02x')
        return((field))        

    def getFileSize(self):
        """ Return file size in bytes """
        return(self.fieldToDec(self.fileHeader.fileSize))

    def getImageWidth(self):
        """ Return image width """
        return(self.fieldToDec(self.DIBHeader.bitmapWidth))

    def getImageHeight(self):
        """ Return image height """
        return(self.fieldToDec(self.DIBHeader.bitmapHeight))

    def getImageDepth(self):
        """ Return image colour depth """
        return(self.fieldToDec(self.DIBHeader.colourDepth))

    def getImageSize(self):
        """ Return image size """
        return(self.fieldToDec(self.DIBHeader.imageSize))

    def getHorizontalResolution(self):
        """ Return horizontal resolution """
        return(self.fieldToDec(self.DIBHeader.horizontalResolution))

    def getVerticalResolution(self):
        """ Return vertical resolution """
        return(self.fieldToDec(self.DIBHeader.verticalResolution))

    def getImageWidthMM(self):
        dpm = self.fieldToDec(self.DIBHeader.horizontalResolution)
        pixels = self.fieldToDec(self.DIBHeader.bitmapWidth)
        if dpm == 0 or pixels == 0:
            return(0)
        width = round(pixels / dpm * 1000)
        return(width)

    def getImageHeightMM(self):
        dpm = self.fieldToDec(self.DIBHeader.verticalResolution)
        pixels = self.fieldToDec(self.DIBHeader.bitmapHeight)
        if dpm == 0 or pixels == 0:
            return(0)
        height = round(pixels / dpm * 1000)
        return(height)

    def getNumberOfColours(self):
        """ Return vertical resolution """
        n = self.fieldToDec(self.DIBHeader.numberColours)
        if n == 0:
            return(2 ** self.getImageDepth())
        else:
            return(n)

    def metreToInch(self,metres):
        return(int(metres / 39.37007874))

    def getCompressionMethod(self):
        """ Return image height """
        c = self.fieldToDec(self.DIBHeader.imageSize)
        if c == 0:
            return("BI_RGB")
        elif c == 1:
            return("BI_RLE8")
        elif c == 2:
            return("BI_RLE4")
        elif c == 3:
            return("BI_BITFIELDS")
        elif c == 4:
            return("BI_JPEG")
        elif c == 5:
            return("BI_PNG")
        elif c == 6:
            return("BI_ALPHABITFIELDS")
        elif c == 11:
            return("BI_CMYK")
        elif c == 12:
            return("BI_CMYKRLE8")
        elif c == 13:
            return("BI_CMYKRLE4")
        else:
            return("UNKNOWN")

    def __str__(self):
        infoStr = ""
        infoStr += "File                  : " + self.fileName + "\n"
        infoStr += "File size             : " + str(self.getFileSize()) + " bytes\n"
        infoStr += "Image width           : " + str(self.getImageWidth()) + " pixels\n"
        infoStr += "Image height          : " + str(self.getImageHeight()) + " pixels\n"
        infoStr += "Colour depth          : " + str(self.getImageDepth()) + " bit\n"
        infoStr += "Image size            : " + str(self.getImageSize()) + "\n"
        infoStr += "Compression method    : " + str(self.getCompressionMethod()) + "\n"
        infoStr += "Bitmap Type           : " + str(self.DIBHeaderType) + "\n"
        infoStr += "Horizontal resolution : " + str(self.getHorizontalResolution()) + " DPM\n"
        infoStr += "Horizontal resolution : " + str(self.metreToInch(self.getHorizontalResolution())) + " DPI\n"
        infoStr += "Vertical resolution   : " + str(self.getVerticalResolution()) + " DPM\n"
        infoStr += "Vertical resolution   : " + str(self.metreToInch(self.getVerticalResolution())) + " DPI\n"
        infoStr += "Number of colours     : " + str(self.getNumberOfColours()) + "\n"
        infoStr += "Image width           : " + str(self.getImageWidthMM()) + " mm\n"
        infoStr += "Image height          : " + str(self.getImageHeightMM()) + " mm\n"
        return(infoStr)

from graphics import *

picture = BMP("C:/Users/Andy/Pictures/test2.bmp")
print(picture)
window = GraphWin("BMP Test", picture.getImageWidth(), picture.getImageHeight())
imageData = picture.imageData

for y in range(len(imageData)):
    for x in range(len(imageData[y])):
        red, green, blue = imageData[y][x]
        colour = color_rgb(red, green, blue)
        p = Point(x,y)
        #print(imageData[y][x])
        p.setOutline(colour)
        p.draw(window)
        
        
