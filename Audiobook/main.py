# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 03:18:17 2020

@author: PRANIKP


Audiobook, that takes PDF file path as input and reads the text in the PDF file 
to the user via audio. Python libraries such as pyPDF2 and pyttsx3 was used in 
implementation.
"""

import pyttsx3
import PyPDF2
book = open('OOP.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    
    