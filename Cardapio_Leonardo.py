import os
os.system("cls||clear")
list_opcoes = []

#Processando dados:
def pagamento(total:float,opcao:int):
    soma = sum(total)
    desconto = soma * 0.1
    if opcao == 1:
        #A vista:
        total_bruto = soma
        total_desconto = soma - desconto
        print("\033[32mForma de pagamento: A vista\033[m")
        print(f"\033[32mTotal: {total_bruto:.2f} R$\033[m")
        print(f"\033[32mDesconto : {desconto:.2f} R$\033[m")
        print(f"\033[32mValor a pagar: {total_desconto:.2f} R$\033[m")
    else:
        #A prazo:
        total_bruto = soma
        total_acrescimo = soma + desconto
        print("\033[32mForma de pagamento: A Prazo\033[m")
        print(f"\033[32mTotal: {total_bruto:.2f} R$\033[m")
        print(f"\033[32mAcréscimo: {desconto:.2f} R$\033[m")
        print(f"\033[32mValor a pagar: {total_acrescimo:.2f} R$\033[m")

def selecao_prato(opcao):
    list_valores = []
    list_pratos=[]
    for item in opcao:
        if item == 1:
            pizza = 25.90
            list_valores.append(pizza)
            list_pratos.append("Pizza        | 25,90 R$")
        elif item == 2:
            churrasco = 19.90
            list_valores.append(churrasco)
            list_pratos.append("Churrasco    | 19,90 R$")
        elif item == 3: 
            lasanha = 23.90
            list_valores.append(lasanha)
            list_pratos.append("Lasanha      | 23,90 R$")
        elif item == 4:
            cerveja = 10.90
            list_valores.append(cerveja)
            list_pratos.append("Cerveja      | 10,90 R$")
        elif item == 5:
            refrigerante = 7.90
            list_valores.append(refrigerante)
            list_pratos.append("Refrigerante |  7,90 R$")
        elif item == 6:
            agua=5.90
            list_valores.append(agua)
            list_pratos.append("Água         |  5,90 R$")
        elif item == 7:
            combo=90.00
            list_valores.append(combo)
            list_pratos.append("Combo        | 90,00 R$")
    return list_pratos, list_valores

#Solicitando dados: Escolhendo pratos.
while True:
    while True:
        opcao =int(input("""
\n\033[4;31m========== CARDÁPIO ===========\033[m\n
\033[37mCOD |  ITEM        |     VALOR
1   | Pizza        |   25,90 R$
2   | Churrasco    |   19,90 R$
3   | Lasanha      |   23,90 R$
4   | Cerveja      |   10,90 R$
5   | Refrigerante |   7,90  R$
6   | Água         |   5,90  R$ 
7   | Combo        |   90,00 R$\033[m
\n\033[4;31mInforme o item desejado:\033[m """))
        list_opcoes.append(opcao)
        if (opcao >= 1) and (opcao<=7):
            break
        else:
            print(f"\033[31mCódigo de prato inválido, informe o código novamente.\033[m")
    retorn = int(input("""\033[31mVocê deseja adicionar outro item ?\033[m
                       \033[31m0 - Para não
                       1 - Para sim
                       : \033[m"""))
    os.system("cls||clear")
    if (retorn == 0):
        lista_pratos, lista_valores = selecao_prato(list_opcoes)
        break
    else:
        print("")

#Solicitando dados: Pagamento.
while True:
    while True:
        opcao1 =int(input("""
\n\033[4;31m========== PAGAMENTO ===========\033[m\n                          
1 - A vista : 10% de desconto\n
2 - Credito : 10% de acrescimo 
\n\033[4;31mInforme a opção desejado: \033[m\n"""))
        if (opcao1 == 1) or (opcao1==2):
            pagamento(lista_valores,opcao1)
            break
    for i,item in enumerate(lista_pratos):
        print(f"\033[32m{i+1}º item : {item}")
    break