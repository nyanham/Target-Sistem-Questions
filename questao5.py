"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada atraves de qualquer entrada de sua preferência ou pode ser previamente definida no codigo;
b) Evite usar funcoes prontas, como, por exemplo, reverse;
"""


str = input("digite uma string: ")

string_invertida = []
i = len(str)

while i > 0: 
    string_invertida += str[i-1]
    i = i - 1
    
string_invertida = ''.join(string_invertida)
print("A string invertida é: ", string_invertida)