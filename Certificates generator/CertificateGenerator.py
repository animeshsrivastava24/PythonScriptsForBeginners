#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd

#this helps with the formatting of text, images
from PIL import Image, ImageDraw, ImageFont

#loading the data
#replace ./Names.xlsx with the path to your file
data = pd.read_excel ('./Names.xlsx') 

#replace Name with the column containing the names in your file
#assigning the name, date and signature with their respective fonts and font size
for i in data["Name"]:
    if len(i)>20:
        #you can change the font size and font url according to your taste
        font_size = ImageFont.truetype(r"c:\users\latee\appdata\local\microsoft\windows\fonts\product sans 400.ttf", 120)
    else:
        font_size = ImageFont.truetype(r"c:\users\latee\appdata\local\microsoft\windows\fonts\product sans 400.ttf", 100)
    im = Image.open('./certificate.png')
    d = ImageDraw.Draw(im)

    #the values should be changed to fit your text appropriately
    name_location = (1272, 1210)
    signature = (786, 1800)
    date = (2050, 1800)
    text_color = (0, 0, 0)
    font = ImageFont.truetype(r"c:\WINDOWS\FONTS\ITCEDSCR.ttf", 120)
    d.text(name_location, i, fill = text_color, font = font_size)
    d.text(signature, "CinnamonXI", fill = text_color, font = font)
    d.text(date, "01-10-2020", fill = text_color, font = font_size)
    im.save(i + ".png")


#if you encounter any issue you can reach our on twitter twitter.com/CinnamonXi


