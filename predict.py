import tesserocr
from PIL import Image

class ocr:
    def __init__(self, filename):
        #self.filename = filename

        self.filename = "inputImage.jpg"

    def getPrediction(self):
        image = Image.open(self.filename)
        lines = tesserocr.image_to_text(image)  # print ocr text from image
        #for line in lines.split("\r"):
            #print(line)
        print(lines)    
        return lines
        

