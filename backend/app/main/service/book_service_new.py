from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
from gtts import gTTS 
import playsound
import shutil

fileaddr = "/home/jay/KWOC/ConnectAll/backend/app/main/service/pdfExample.pdf"
pages = convert_from_path(fileaddr,500)

original_cwd=os.getcwd()
directory_name = 'pdfImages'
os.mkdir(directory_name)
os.chdir(original_cwd+'/'+directory_name)

image_counter = 1

for page in pages:
    filename = 'page_'+str(image_counter)+'.jpg'
    page.save(filename,'JPEG')
    image_counter += 1

totalpages = image_counter - 1
outfile = 'content.txt'
f = open(outfile,'a')

for page_no in range(1,totalpages+1):
    filename = 'page_'+str(page_no)+'.jpg'
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text)
f.close() 

text_file = open(outfile, "r").read().replace("\n", " ")
language = 'en'

audio_file = gTTS(text=text_file, lang=language)

os.chdir(original_cwd)
shutil.rmtree(original_cwd+'/'+directory_name)

audio_file.save('pdfsample.mp3')


playsound.playsound('pdfsample.mp3', True)