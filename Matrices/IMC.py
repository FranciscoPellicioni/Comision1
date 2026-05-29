#Crear un programa que calcule el Índice de Masa Corporal (IMC) de una persona usando funciones.
#IMC = peso / (altura * altura)
#Las funciones deben ser:
#• pedir_datos() → pide y retorna peso y altura
#• calcular_imc(peso, altura) → retorna el IMC
#• clasificar(imc) → retorna: Bajo peso / Normal / Sobrepeso / Obesidad

def pedir_datos(peso,altura):
    peso = float(input("Ingrese su peso corporal: "))
    altura = float(input("ingrese su altura en metros: "))

    return peso,altura

def calcular_imc(peso,altura,IMC):
    IMC = peso/(altura * altura)

    return IMC

def clasificar(IMC,pesof):
    if IMC < 18.5:
        pesof = "Bajo peso"
    elif 18.5 <= IMC < 25:
        pesof = "Normal" 
    elif 25 <= IMC < 30:
        pesof = "Sobrepeso"
    else:
        pesof = "Obesidad"

    return pesof

def mostrar(pesof,IMC):
    print("EL IMC ES:",IMC)
    print("CLASIFICACION:", pesof)

def iniciar():
    peso = 0
    altura = 0
    IMC = 0
    pesof = ""

    peso,altura = pedir_datos(peso,altura)
    IMC = calcular_imc(peso,altura,IMC)
    pesof = clasificar(IMC,pesof)
    mostrar(pesof,IMC)

iniciar()