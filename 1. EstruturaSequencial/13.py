# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando 
# as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

height = float (input("Insira a sua altura: "))
man_weight = (72.7*height) - 58
woman_weight = (62.1*height) - 44.7

print (f"""
Caso você seja HOMEM, seu peso ideal é de: {man_weight:,.2f}kg
Caso você seja MULHER, seu peso ideal é de: {woman_weight:,.2f}kg    
""")