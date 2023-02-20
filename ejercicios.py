

""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

def HACIENDOELTRABAJODEESSA ():
    ValorKW= 315.6
    print("\tBienvenido a la calculadora de deudas con ESSA :3. Por favor ingresar los siguientes datos:")
    MesdeConsumo = str(input("Ingresa el mes de la factura  <"))
    Estrato = int(input("Ingresa el estrato que perteneces  <"))
    TotalKw = int(input("Ingresa el total de  Kw consumidos en el mes  <"))
    valorTotal= ValorKW*TotalKw
    if Estrato == 1:
        descuento=valorTotal*0.6
    if Estrato == 2:
        descuento=valorTotal*0.5
    if Estrato == 3:
        descuento=valorTotal*0.15
        
    print("El valor total a pagar por la electricidad consumida en", MesdeConsumo , "\n segun el estrato registrado" , (Estrato) ,"es", valorTotal-descuento )
    
    return()
    
    
HACIENDOELTRABAJODEESSA()