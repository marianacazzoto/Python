# Trabalhando com Strings

minha_string = "qualquer texto"
print(f"concatenar {minha_string} em string")

print(minha_string.upper()) #Transforma todas as letras em maiusculas
print(minha_string.lower()) #Tranforma todas as letras em minusculas
print(minha_string.capitalize()) #Transforma a primeira letra em maiuscula
print(minha_string.isupper()) #Retorna um booleano,verificando se letras estão maiuscula
print(minha_string.islower()) #Retorna um booleano,verificando se letras estão minusculas
print(minha_string.strip()) #Remove os espaços em brancos
print(minha_string.replace("qualquer", "meu")) #Substituí as palavras que deseja
print(minha_string.replace("u", "U",1))  #Substituí as palavras pela quantidade que marcou
print(len(minha_string)) #Retorna o tamanho da string 
print(minha_string[2]) #Retorna o index

x = "texto" in minha_string #Retorna se na variavel realmente tem uma palavra "texto"

print(x)
