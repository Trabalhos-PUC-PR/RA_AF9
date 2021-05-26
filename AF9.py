'''
1) Desenvolva uma App em Python para ler um conjunto de 20 valores inteiros digitado no teclado e que gere uma outra lista 
com a soma dos elementos equidistantes. Ao final, App deverá imprimir as duas listas. Exemplo de uma lista com 6 elementos.
Lido lista A = 1, 2, 3, 4, 5, 6 Calculado lista B= 7, 7, 7

2) Desenvolva uma App em Python para somar as duas listas abaixo e gera uma terceira com o resultado. Ao final, a App deverá
imprimir as três listas. A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54] B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] 

3) Desenvolver uma App em Python para gerar e imprimir uma lista com os 100 primeiros números inteiros de 1 até 100.

4) Desenvolver uma App em Python para gerar e imprimir uma lista com os 50 primeiros números pares de 1 até 100.

5) Desenvolva uma App em Python que leia um número N inteiro do teclado. Em seguida, leia N números inteiros digitados e guarde 
numa lista. Ao final, crie e imprima uma lista com os valores maiores que 3, os pares, os divisíveis por 5 e a soma dos ímpares.
'''
import numpy as np

escolha = int(input("Escolha a atividade (1-5): "))
if(escolha>5 or escolha<1):
    exit("Atividade não existente")

#---------------------------------------------------------------ATIVIDADE 1
if(escolha == 1):
    lista = [] #declaração lista que recebe os valores digitados
    for i in range(1, 21): #for que repete do 1 ao 20 (ele pula o 21 :/)
        lista.append(int(input("Digite um numero: "))) #cria um novo elemento na lista com o numero
    lista_2 = [] #declarar lista pra receber a soma da primeira
    for i in range(0, int(len(lista)/2)): #pega metade da primeira lista
        lista_2.append((lista[i] + lista[19-i])) #ele pega os extremos, i, o menor extremo, e 19 - i, o maior index - a posição contraria, e coloca no vetor lista_2
    print("Números recebidos", lista) #printa a primeira lista
    print("Números somados", lista_2) #printa a segunda lista somada
    exit()

#---------------------------------------------------------------ATIVIDADE 2
if(escolha == 2):
    A = [1, 2, 3, 4, 5, 6, 7, 10, 25, 54] #lista que o professor passou
    B = [20, 25, 14, 67, 5, 12, 75, 54, 32, 10] #lista que o professor passou
    C = [] #lista que recebe a soma das duas
    #print(len(A)) #teste para checar quantas posições essas listas tem (elas tem o mesmo tamanho)
    #print(len(B)) #teste para checar quantas posições essas listas tem (elas tem o mesmo tamanho)
    for i in range(0, len(A)): #para i dentro do raio de 0 até 10:
        C.append(A[i] + B[i]) #coloca na lista C a soma de A e B
    print(A) #print da lista A
    print(B) #print da lista B
    print(C) #print da lista C
    exit()

#---------------------------------------------------------------ATIVIDADE 3
if(escolha == 3):
    lista = [] #lista que recebe os valores
    for i in range(1, 101): #for que repete de 1 até 100
        lista.append(i) #coloca na lista lista o valor i
    print(lista) #print da lista
    exit()

#---------------------------------------------------------------ATIVIDADE 4
if(escolha == 4):
    lista = [] #lista que recebe os valores
    for i in range(1, 101): #for que repete de 1 até 100
        if(i % 2 == 0): #se a divisão por 2 devolve 0
            lista.append(i) #coloca na lista lista o valor i
    print(lista)
    exit()

#---------------------------------------------------------------ATIVIDADE 5
if(escolha == 5):
    valor = int(input("Digite um número qualquer: "))
    lista_maior = [] # lista pros numeros maiores que 3
    lista_par = [] # lista pros numeros pares
    lista_divisivel = [] # lista pros numeros divisiveis por 5
    soma_impar = 0 # lista pros numeros impares somados
    for i in range(0, valor+1): #para i dentro do raio de 0 até o valor digitado (sem o +1 vai até o valor digitado -1)
        if(i > 3): #se i valor atual é maior que 3
            lista_maior.append(i) #coloca na lista "lista_maior"
        if(i % 2 == 0): #se o valor mod 2 é igual a 0 (se resta 0 na divisão)
            lista_par.append(i) #coloca na lista "lista_par"
        if(i % 5 == 0): #se o valor mod 5 é igual a 0 (divisivel por 5)
            lista_divisivel.append(i) #coloca na lista "lista_divisivel"
        if(i % 2 != 0): #se não é par (valor mod 2 igual a 0)
            soma_impar += i #soma com a variavel "soma_impar" (achei estranho declarar uma lista pra ter só uma posição)
    print("O valor escolhido foi: ",valor) #print do valor digitado
    print("A lista dos números maiores que 3: ",lista_maior) #print dos numeros maiores que 3
    print("A lista dos números pares: ",lista_par) #print dos numeros pares
    print("A lista dos números divisiveis por 5: ",lista_divisivel) #print dos numeros divisiveis por 5
    print("A soma dos itens ímpares: ",soma_impar) #print da soma dos impares
    exit()