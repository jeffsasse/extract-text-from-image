# Import required packages
import cv2
import pytesseract
import os,argparse
from PIL import Image
 
# Mention the installed location of Tesseract-OCR in your system
tesseract_path = r"/usr/local/Cellar/tesseract/5.3.2_1/bin/tesseract"

pytesseract.pytesseract.tesseract_cmd = tesseract_path
out_put_file = r"output.txt"
img_path = r"images/sample.png"
 
# Read image from which text needs to be extracted
img = Image.open(img_path)
 
# A text file is created and flushed
file = open(out_put_file, "w+")
file.write("")
file.close()

text = pytesseract.image_to_string(img)

file = open(out_put_file, "a")
# Appending the text into file
file.write(text)
file.write("\n")
    
# Close the file
file.close