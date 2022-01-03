#Função Soma
def soma(n1, n2):
    resultado = n1 +n2
    return resultado

#Função Subtração
def subtracao (n1, n2):
    resultado = n1 - n2
    return resultado

#Função Multiplicação
def multiplicacao (n1, n2):
    resultado = n1 * n2
    return resultado

#Função Divisão
def divisao(n1, n2):
    resultado = n1 / n2
    return resultado

print ("Seja bem vindo ao jogo Matemático!")

control = True

while (control == True):

    n1 = float(input ("Insira o primeiro número: "))
    n2 = float(input ("Insira o segundo número: "))

    print ("Selecione uma das operações: ")
    operador = int(input("1) Adição \n2) Subtração \n3) Multiplicação \n4) DIvisão.\n R.:"))

    if(operador == 1):
        soma = soma(n1,n2)
        print (soma)

    if(operador == 2):
        subtracao = subtracao(n1,n2)
        print (subtracao)

    if(operador == 3):
        multiplicacao = multiplicacao(n1,n2)
        print (multiplicacao)

    if(operador == 4):
        divisao = divisao(n1,n2)
        print (divisao)

    if (operador > 4):
        print("Posição inexistente, reinicie o sistema e insira uma operação válida.")

    control2 = input("Deseja continuar? S/N\n R.:")
    if (control2.upper() =="S"):
        control = True
    else:
        control = False

        
