def calcular_media(valores):
    return sum(valores) / len(valores)


valores = [float(input(f"Digite o valor {i+1}: ")) for i in range(4)]
media = calcular_media(valores)
print(f"A média dos valores é: {media:.2f}")
