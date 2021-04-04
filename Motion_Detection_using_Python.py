from tkinter import * 
from tkinter.font import Font
from tkinter import massagebox
import numpy as np
import cv2
import time
import sys
import os, signal
import smtplib
from urlib.request import urlopen

email_id = 'piykuz@gmail.com'
Path = os.path.abspath(os.getcwd())+r'\Recording'

def isconnected():
  try:
    urlopen('http://216.58.192.142')
    return True
  except:
    return false
  
  def Email_sender():
    global email_id
    try:
      s = ssmtplibSMTP('smtp.gmail.com', 587)
      
      # start TLS for security
      s.starttls()
      
      # Authentication 
      s.login("piy.k.21@gmail.com", "1a4nN@21")
      
      # message to be sent
      
      message = "Intruder ALERT! Someone is Detected in your Room"
      
      s.sendemail("piy.k.21@gmail.com", email_id, message)
      s.quit()
    except:
      pass
    finally:
      return
    
    
    def detectmotion():
