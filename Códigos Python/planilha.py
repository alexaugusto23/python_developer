import pandas as pd

list_dureza = []        
list_volume = []
saida = True

while saida:
    dureza = float(input("Informe a dureza: "))
    if dureza >= 0 and dureza <=20:
        list_dureza.append(dureza)
        print('leve')
    elif dureza >= 20 and dureza <=50:
        volume = float(input('informar o volume da caixa d´gua: '))
        volume *= 1000
        list_volume.append(volume)
        print(f'aumentar dreno em litros {volume}') 

    saida = input("Deseja sair no sistema sim ou não: ")
    if saida == 'sim':
        saida = False
        print("saindo do sistema")


planilha = pd.DataFrame(data=list(zip(list_dureza,list_volume)), index=None, columns=['Dureza', 'Volume'], dtype=None, copy=None)  
print(planilha)    

planilha.to_excel("planilha_filtros.xlsx", sheet_name='filtros') 
    

