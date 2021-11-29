'''
Instalar as seguintes bibliotecas:

pip install pyttsx3
pip install pyaudio
pip install beautifulsoup4

'''

import pyttsx3
import speech_recognition as sr
import os
import pyaudio
from urllib.request import urlopen
import json
import webbrowser
from datetime import datetime
import csv
from bs4 import BeautifulSoup
import requests

assistente = pyttsx3.init()
recon = sr.Recognizer()
inpvoz = ""


# Funções
def retorno(frase):
    assistente.say(frase)
    assistente.setProperty('voice', b'brasil')
    assistente.setProperty('rate', 280)
    assistente.setProperty('volume', 1)
    assistente.runAndWait()


def ouvir():
    recon.adjust_for_ambient_noise(source)
    audio = recon.listen(source)
    inpvoz = recon.recognize_google(audio, language="pt-BR")
    return inpvoz



# Reconhecimento de voz e ações
with sr.Microphone() as source:
    recon.adjust_for_ambient_noise(source)
    retorno(
        'Olá! Sou a assistente virtual Claro Box e vou auxiliar sua experiência com nossos serviços. O que você deseja fazer?')
    print('Olá! Sou a assistente virtual Claro Box e vou auxiliar sua experiência com nossos serviços. O que você deseja fazer?')

    while True:
        try:
            acao = str(ouvir())
            print("Você disse: " + acao)
           


            frase_continuar = "Posso ajudar com algo mais? Responda sim para continuar e não para finalizar!"
            retorno(frase_continuar)
            acao = str(ouvir())
            print(f'Você disse {acao}')
            
            if 'não' in acao:
                retorno('Espero ter ajudado! Até mais!')

                break
            else:
                retorno('No que posso te ajudar?')
        except:
            retorno('Desculpe, não entendi. poderia repetir por favor?')
