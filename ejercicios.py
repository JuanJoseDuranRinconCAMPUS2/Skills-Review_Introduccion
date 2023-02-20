from colorama import init, Fore, Back, Style

""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

def Datos():
    actual= int(2023)
    print(Fore.MAGENTA+"Hola BIenvenido, Ingresa tus datos Por Favor ;3")
    Nombre=str(input(Fore.BLUE+"Ingresa tu nombre completo sin apellidos <"))
    Apellidos=str(input(Fore.BLUE+"Ingresa tus Apellidos <"))
    Edad=int(input(Fore.BLUE+"Ingresa tu Edad <"))
    AñoDeImgreso=int(input(Fore.BLUE+"Ingresa el año que ingresaste a nuestra empresa <"))
    permiso=int(input("¿Quieres ver tus datos mas importantes?   1.Si 2.No <"))
    if permiso == 1:
        print(Fore.GREEN+"Tus Datos de usuario son: \n Nombre y Apellidos:" , Nombre, Apellidos, "\nAño de ingreso a nuestra empresa:", AñoDeImgreso, "\n Tiempo en la empresa:", {actual-AñoDeImgreso})
    return(Nombre, Apellidos, Edad, AñoDeImgreso)
    
Datos()
