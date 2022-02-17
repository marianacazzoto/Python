def sptech(turma):
    print(f"Turma 2021/2 - {turma}")

def coordenadores(nome):
    print(f"Nome da coordenadora: {nome}")

def conclusao(ano):
    print(f"Ano de conlusão - {ano}")

def juncao_de_dados(turma,nome,ano):
    sptech(turma)
    coordenadores(nome)
    conclusao(ano)

#juncao_de_dados("1adsb","Kaline","2023")

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,20)
#print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num 

resultado = maior_num([321,654,68,798,2,165,-1,52,-46,-3654,2,7])
print(resultado)





