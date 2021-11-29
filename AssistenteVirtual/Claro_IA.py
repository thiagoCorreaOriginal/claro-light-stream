'''
Instalar as seguintes bibliotecas:

pip install pyttsx3
pip install pyaudio
pip install beautifulsoup4
pip install SpeechRecognition

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
           
            if 'disney' in acao.lower():
                servico_escolhido = 'https://www.disneyplus.com/pt-br/home'

                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

                webbrowser.get(chrome_path).open(servico_escolhido)

            if 'marvel' in acao.lower():
                servico_escolhido = 'https://www.disneyplus.com/pt-br/brand/marvel'

                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

                webbrowser.get(chrome_path).open(servico_escolhido)     

            if 'gavião arqueiro' in acao.lower():            
                servico_escolhido = 'https://www.disneyplus.com/pt-br/series/gaviao-arqueiro/11Zy8m9Dkj5l'

                chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

                webbrowser.get(chrome_path).open(servico_escolhido)   

            if 'onde' in acao.lower() or 'jogo' in acao.lower() or 'imitação' in acao.lower():            
                frase_retorno = "O Filme \'o jogo da imitação\' pode ser visto nas plataformas HBO Max e Amazon Prime Video"
                print(frase_retorno)
                retorno(frase_retorno)
                frase_retorno_2 = "Ele também pode ser alugado por 2 reais e 90 centavos no Youtube, Google Play e Apple TV"
                print(frase_retorno_2)
                retorno(frase_retorno_2)
                   

            frase_continuar = "Posso te ajudar em mais alguma coisa? Fale \'não\' caso não precise de mais ajuda"
            retorno(frase_continuar)
            acao = str(ouvir())
            print(f'Você disse {acao}')
            
            if 'não' in acao.lower():
                retorno('Espero ter ajudado! Até mais!')

                break
            else:
                retorno('No que posso te ajudar?')
        except:
            retorno('Desculpe, não entendi. Ainda estou aprendendo')
            break
