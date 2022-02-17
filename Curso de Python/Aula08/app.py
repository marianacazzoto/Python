#tenho_sede = True

#if tenho_sede:
#    print("Beber água")

# esta_frio = True

""" if esta_frio:
    print("Vestir um casaco")

else:
    print("Vestir camiseta") """

from tkinter import E


tenho_sede = True
tenho_fome = True
estou_em_dieta = True

""" if tenho_sede or tenho_fome:
    print("vou na cozinha")
else:
    print("ficar vendo netflix") """

""" if tenho_sede and tenho_fome:
    print("fazer sandíche e coca")
else:
    print("não tenho fome ou não tenho sede") """

if tenho_sede and tenho_fome:
    print("fazer sandíche e coca")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("tomar agua")
    else:
        print("tomar uma coquinha")    
elif not(tenho_sede) and tenho_fome:
    print("Fazer um sanduíche")
else:
    print("ficar vendo netflix")

num1 = 5
num2 = 32

if num1 == num2:
    print("num1 é igual a num2")
#elif num1 != num2:
    #print("num1 é diferente de num2")
elif num1 > num2:
    print("num1 é maior que num2")
elif num1 < num2:
    print("num1 é menor que num2")

#operadores logicos 
#or = ou
#and = e
#not() = negação


