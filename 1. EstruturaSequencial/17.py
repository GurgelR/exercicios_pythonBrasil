# =============================================================================
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# 
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:
# 
#       a) comprar apenas latas de 18 litros;
#       b) comprar apenas galões de 3,6 litros;
#       c)misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#       Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#       considere latas cheias.
# =============================================================================

area_pintada = float (input ("Digite a área a ser pintada em m²: "))
preco_litro_galao = 25/3.6
preco_litro_lata = 80/18

print(preco_litro_galao)
print(preco_litro_lata)


