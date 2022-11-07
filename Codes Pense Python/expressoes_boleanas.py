print(f"5==5 bool tipo: {type(5==5)}")
print(f"5==5: {5==5}")
print(f"5==6: {5==6}")

print()

try: 
    x = float(input("Digite o valor X: "))
    y = float(input("Digite o valor Y: "))
    a = x

    print()
    print(f"a = x: {a} \n a:{a} recebe o valor x:{x} por atribuição\n") 
    print(f"x == y: {x == y} \n{x} é igual a {y}\n") 
    print(f"x != y: {x != y} \n{x} não é igual a {y}\n") 
    print(f"x > y: {x > y}   \n{x} é maior que {y}\n")
    print(f"x < y: {x < y}   \n{x} é menor que {y}\n")
    print(f"x >= y: {x >= y} \n{x} é maior ou igual que {y}\n")
    print(f"x <= y: {x <= y} \n{x} é menor ou igual que {y}\n")


except ValueError as err: print(f"{err}")