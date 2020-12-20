# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:42:10 2020


Project Name: Automate Whatsapp message.

Description: This project will allow us to automatically send whataspp messages to an individual 
             or a group in whatApp. 
             Prequesits: After executing the progrm , we need to make sure browser is opened in our system.
             
             1) Here we provide the contact number to whom we want to send the message along with the 
                message that needs to be sent. And we also set the time at which we want the message to be delivered.
                
            2) Once the program is executed , at the provided time the whatsApp will be opened in the browser and 20 sec after 
               browser is opened the message will be sent to the individual or group.
               
Library Used: pywhatkit
    
@author: PRANIKP
"""

import pywhatkit

individual_group_ind = input("Please enter (I) for indivial message or (G) for group message:")

contact_info = str(input("Please prove the contat number or group ID:"))
text = str(input(" Please input the message:"))


if individual_group_ind == 'I':
    pywhatkit.sendwhatmsg(contact_info, text, 22,6)
    pywhatkit.sen
else:
    pywhatkit.sendwhatmsg_to_group(contact_info, text, 22,9)