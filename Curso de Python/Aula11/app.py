#  Tratando exceção - Try,Except,Finally
try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Digite um valor valido")
finally:
    print("Sempre executa")