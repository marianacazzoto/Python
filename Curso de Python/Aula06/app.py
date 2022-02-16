familia = ["Lucia","Mariana","Maria Luiza","Daniel","Gabriel"]

#print(familia[3]) #Retorna um indice 
#print(familia[-3]) #Retorna um indice de traz pra frente
#print(familia[2:]) #Retorna a partit do indice 2
#print(familia[2:4]) #Retorna a patir do indice 2 até o 4,excluindo o 4

#print(familia)

familia[0] = "Lucia Maria" #Altera o indice
#print(familia)

familia.extend(["Sandra","Cristiano"]) #.extend juntas todas as listas em uma só

familia.append("Sheik")#.append adciona um registro só
familia.insert(1,"Lara") #você escolhe em qual indice quer colocar 
#print(familia)

familia.pop() #remove o ultimo indice
#print(familia)

familia.remove("Lara")#Remove o nome que escolher
#print(familia)

#familia.clear() #remove todos os itens da lista
#print(familia)

#print(familia.count("Mariana"))#retorna quantos valores iguais temos na lista

idade_familia = [19,17,41,23,25]
print(idade_familia)

idade_familia.sort() #ordena a idade do menor para o maior
                     #.sort funciona tanto para inteiro quanto para strings
print(idade_familia)
