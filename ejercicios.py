from colorama import init, Fore, Back, Style

""" 8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

numero=input(Fore.MAGENTA+"Ingresa un numero plis :3      ")
numero=int(numero)

if int(numero) == numero:
    if numero %2== 0:
        if numero >20:
            print("El dato es un numero par y es mayor o igual a 20")
        else:
            print("El dato es un numero par menor que 20")
    else:
        print("El dato es un numero y es impar")

else:
    print("te dije que digitaras un numero >:c")
