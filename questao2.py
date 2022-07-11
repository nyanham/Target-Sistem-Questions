"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o proximo valor sempre sera a soma
dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa
na linguagem que desejar onde, informado um numero, ele calcule a sequencia de Fibonacci e retorne
uma mensagem avisando se o numero informado pertence ou nao a sequencia.

IMPORTANTE:
Esse numero pode ser informado atraves de qualquer entrada de sua preferencia ou pode ser
previamente definido no codigo;
"""

import math 
   
# Aqui, vamos verificar se K e um quadrado perfeito
def quadrado_perfeito(K):  
    s = int(math.sqrt(K))  
    return s * s == K  
   
# Agora, esta funcao ira verificar se R sera fibonacci  
def Fibonacci(R):  
   
    # Para um numero ser fibonacci, uma das duas funcoes (5 * R * R + 4) e (5 * R * R - 4)
    # devem ser quadrado perfeito
    return quadrado_perfeito(5 * R * R + 4) or quadrado_perfeito(5 * R * R - 4)  
      
# Funcao main 
def main():
    try:
        while True:
            n = int(input("Digite o valor a ser verificado ou Ctrl+C para sair: "))
            if (Fibonacci(n)):  
                print ("O numero digitado pertence a fibonacci")  
            else:  
                print ("o numero digitado nao pertence e fibonacci")
    except KeyboardInterrupt:
        print("\nbye")
        pass

if  __name__ == "__main__":
    main()