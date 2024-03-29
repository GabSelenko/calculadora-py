def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)

def potencia():
    x = float(input("primeiro numero: "))
    y = float(input("segundo numero: "))
    print("potencia: ",x**y)

opcao=1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("5, Potencia")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
    if(opcao==5):
        potencia()