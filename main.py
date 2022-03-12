# %% [markdown]
# <a href="https://colab.research.google.com/github/RajiRai/Voice-Assistant/blob/main/Minchu.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
# pip install SpeechRecognition
# pip install wikipedia
# pip install gTTS
# pip install ecapture
# pip install ipython
# pip install pyinstaller
# pip install selenium
# pip install playsound

# %%
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import requests
import pyttsx3
import subprocess #process various system commands like to log off or to restart your system
#from ecapture import ecapture as ec #for capturing photos 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 

# %%
def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
        return data     


# %%
def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    
    playsound.playsound(file, True)  
    os.remove(file)

# %%
if __name__=='__main__':
    respond("Hi, I am Vampire personal Assistant")
      
    while(1):
        
        respond("How can I help you?")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break
            
        if 'wikipedia' in text or 'search' in text:
            respond('Searching Wikipedia')
            #text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        else: 
  
            respond("Application not available") 

# %% [markdown]
# ## 

# %%


# %%


# %%



