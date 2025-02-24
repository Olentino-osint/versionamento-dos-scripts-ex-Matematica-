import math


def area_retangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_circulo(raio):
    return math.pi * (raio ** 2)


base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio do círculo: "))

print(f"Área do retângulo: {area_retangulo(base, altura):.2f}")
print(f"Área do triângulo: {area_triangulo(base, altura):.2f}")
print(f"Área do círculo: {area_circulo(raio):.2f}")
