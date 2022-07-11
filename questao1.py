"""
Observe o trecho de codigo abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faca
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);

Ao final do processamento, qual sera o valor da variavel SOMA?
"""


s = 0
k = 0

for i in range(13):
    k += 1
    s = s + k
print(s)