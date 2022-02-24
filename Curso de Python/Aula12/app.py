#Manipulando Arquivos

#Modos
#r - leitura
#a - Append/ incrementar
#w - escrita - limpa o arquivo antigo e começa a escrever
#x - criar aquivos
#r+ - leitura + escrita

#open("caminho","r")
#arquivo = open("Aula12/teste2.txt","a")

#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())

#arquivo.write("Python") #adciona na lista teste.txt

#arquivo.close()

import os

os.remove("Aula12/teste2.txt")
