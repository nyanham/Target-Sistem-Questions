"""3) Dado um vetor que guarda o valor de faturamento diario de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mes;
• O maior valor de faturamento ocorrido em um dia do mes;
• Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal.

IMPORTANTE:
a) Usar o json ou xml disponivel como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias
devem ser ignorados no calculo da media;
"""

import json

#Abrindo o arquivo json
with open("dados.json", encoding='utf-8') as arquivo_json:
    datas = json.load(arquivo_json)

#total_faturamento e dia_faturamento serao usados para extrair a media do mes
#faturamento_teto e faturamento_piso sao o maior e menor valor de faturamento ocorrido em um dia no mes
total_faturamento = 0
dia_faturamento = 0
faturamento_teto = datas[0]['valor']
faturamento_piso = datas[0]['valor']

for valor in datas:
    if(valor['valor'] != 0):
        dia_faturamento = dia_faturamento + 1
        total_faturamento = total_faturamento + valor['valor']
  
        if(faturamento_teto < valor['valor']):
            faturamento_teto = valor['valor']

        if(faturamento_piso > valor['valor']):
            faturamento_piso = valor['valor']
    
media_faturamento = total_faturamento/dia_faturamento

dias_faturamento_maior_media = 0

for valor in datas:
  if valor['valor'] > media_faturamento:
    dias_faturamento_maior_media = dias_faturamento_maior_media + 1

print(f"O menor valor de faturamento ocorrido em um dia do mes foi ${faturamento_piso}")
print(f"O maior valor de faturamento ocorrido em um dia do mes foi ${faturamento_teto}")
print(f"Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal foi {dias_faturamento_maior_media}")