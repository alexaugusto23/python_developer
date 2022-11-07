minutes = 105
div_min = minutes / 60
horas = minutes // 60 # divisão pelo piso devolve a divisão arrendoda para baixo.
minutos_restantes_mod = minutes % 60 # divisão pelo modulo devolve o resto da divisão

restante_de_horas = minutes - ( horas * 60 )

print(f"Divisão de minutos: {div_min}")
print(f"Divisão do minutos pelo piso: {horas}")
print(f"Minutos restantes: {restante_de_horas}")
print(f"Minutos restantes pela divisão modulo: {minutos_restantes_mod}")

try:
    x = float(input("Digite o valor de X: "))
    y = float(input("Digite o valor de Y: "))

    if x % y == 0:
        print(f"O número {x} é divisivel por {y} porque o resto é {x % y}")
    else: print(f"Não é possivel dividir o número {x} por {y}")

except ValueError: print(f"Somente Valores de ponto flutuante")

