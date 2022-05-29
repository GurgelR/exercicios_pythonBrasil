# Faça um Programa que peça o raio de um círculo,
# calcule e mostre sua área.

from math import pi

raio = float (input("Raio do círculo: "))
area = pi*raio**2

print (f"A área do círculo é de: {area:,.2f}")


