# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
# Estes dias devem ser ignorados no cálculo da média;


valor_dia = [31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269,
                      0.0000, 6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000,
                      39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017,
                      0.0000, 0.0000, 12974.2000, 28490.9861, 8748.0937, 8889.0023,
                      17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 10299.6761,
                      39874.1073]

# menor valor em um dia de faturamento
menor_valor = min(valor_dia)
print("Menor valor de faturamento:", menor_valor)

# maior valor em um dia de faturamento
maior_valor = max(valor_dia)
print("Maior valor de faturamento:", maior_valor)

# média mensal
com_faturamento = [faturamento for faturamento in valor_dia if faturamento != 0]
media_mensal = sum(com_faturamento) / len(com_faturamento)

# número de dias no mês em que o valor de faturamento diário foi superior à média mensal
acima_media = sum(1 for faturamento in com_faturamento if faturamento > media_mensal)
print("Número de dias com faturamento acima da média mensal:", acima_media)