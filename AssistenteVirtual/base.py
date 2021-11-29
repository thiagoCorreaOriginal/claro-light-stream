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


def continuar():
    retorno('Posso ajudar com algo mais? Responda sim para continuar e não para finalizar!')
    continuar = ouvir()
    print(f'Você disse {continuar}')
    return continuar


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
            

            # Pesquisa o serviço na api, por exemplo: INSS ou ENEM
            url = f"https://portalunico.estaleiro.serpro.gov.br/api/search/?q={acao.lower()}&ordenacao=-relevancia&categoriasFiltro=&orgaosFiltro=&tipo=Servico%7CTema&pagina=1&tam_pagina=30"

            link = f'gov.br/pt-br/search?SearchableText={acao.lower()}'

            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            # Abre a lista de serviços retornados no chrome e narra
            webbrowser.get(chrome_path).open(link)

            response = urlopen(url)

            data_json = json.loads(response.read())

            items = data_json.get("items")

            retorno('Esses são os 10 principais resultados de pesquisa: ')

            for k, v in enumerate(items[0:10]):
                retorno(f'{k + 1} - {v["title"]}')

            retorno('Diga o número da sua opção: ')

            try:
                escolha = ouvir()
            except:
                retorno('Não entendi! Por favor, repita sua opção.')
                escolha = ouvir()

            while int(escolha) not in range(1, 11):
                retorno('Por favor, escolha a sua opção entre 1 e 10!')
                try:
                    escolha = ouvir()
                except:
                    retorno('Não entendi! Por favor, repita sua opção.')
                    escolha = ouvir()

            # Recebe o número do serviço desejado e abre uma nova guia no chrome
            servico_escolhido = f'https://www.gov.br{items[int(escolha) - 1]["contentUrl"]}'

            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            webbrowser.get(chrome_path).open(servico_escolhido)

            retorno(f'Certo! Aqui você vai encontrar as instruções sobre {items[int(escolha) - 1]["title"]}')

            # Lê a descrição do serviço, caso o usuário solicite
            retorno(f'Deseja que eu leia a descrição?')

            ler = ouvir()

            if str(ler.lower()) in ('sim'):
                html = requests.get(servico_escolhido).content

                soup = BeautifulSoup(html, 'html.parser')

                titulo = soup.find('a', class_="titulo toggle-link", id="dados_basicos").getText()
                conteudo = soup.find('div', class_='conteudo').getText()

                retorno(conteudo)

            cont = continuar()

            if 'não' in cont:
                retorno('Espero ter ajudado! Até mais!')

                break
            else:
                retorno('Qual serviço você deseja pesquisar?')
        except:
            retorno('Desculpe, não entendi. Ainda estou aprendendo.')
