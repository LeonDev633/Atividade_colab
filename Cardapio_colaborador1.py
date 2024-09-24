import os
os.system("cls||clear")
import time

def logo_senai():
    print("""\033[34m
===============
---  \033[37mSENAI\033[34m  ---
===============  \033[m        

""")

#Informando valores:
def cardapio_apresentacao():
    print(""" 
    escreva o codigo do prato para fazer o pedido:
    codigo |alimento        |valor |
          
    1     |Picanha         | 25,90R$ |
    2     |Lasanha         | 20,90R$ |
    3     |Strogonoff      | 18,90R$ |
    4     |Bife acebolado  | 15,90R$ |
    5     |Feijoada        | 50,90R$ |
    6     |Macarronada     | 19,90R$ |
    7     |Bebidas         | 05,90R$ |
        """)
    
#Dados:   
def codigo_card(a):
    if a == 1:
        picanha = 25.90
        return picanha
    elif a == 2:
        lasanha = 20.90
        return lasanha
    elif a == 3:
        strogonoff = 18.90
        return strogonoff
    elif a == 4:
        bife_acebolado = 15.90
        return bife_acebolado
    elif a == 5:
        feijoada = 50.90
        return feijoada
    elif a == 6:
        macarronada = 19.90 
        return macarronada
    elif a == 7:
        bebidas = 05.90
        return bebidas

#Processamento de dados:
def finalizando_compra (a, b):
    desconto = (sum(b))*0.1
    if a == 1:
        soma = sum(b)
        desconto = 0
        return soma, desconto
    elif a == 2:
        soma = sum(b)
        result = soma + (desconto)
        return result, desconto
    elif a == 3:
        soma = sum(b)
        result = soma - desconto
        return result, desconto
    elif a == 4:
        soma = sum(b)
        result = soma - desconto
        return result, desconto
        

carrinho_de_compra=[]
lista_selecao = []

while True:
    logo_senai()
    cardapio_apresentacao()
    while True:
        opcao = int(input("Escolha seu prato: "))
        lista_selecao.append(opcao)
        if (opcao >=1)and(opcao <=7):
            break
        else:
            print("Prato invalido, informe o codigo do prato novamente.")
            time.sleep(2)
    match(opcao):
        case 1:
            picanha=codigo_card(opcao)    
            carrinho_de_compra.append(picanha)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                        : """))
            if opcao2==1:
                opcao
            else:
                break
        case 2:
            lasanha=codigo_card(opcao)
            carrinho_de_compra.append(lasanha)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao
            else:
                break
        case 3:
            strogonoff = codigo_card(opcao)
            carrinho_de_compra.append(strogonoff)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao 
            else:
                break
        case 4:
            bife_acebolado = codigo_card(opcao)
            carrinho_de_compra.append(bife_acebolado)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao
            else:
                break
        case 5:
            feijoada = codigo_card(opcao)
            carrinho_de_compra.append(feijoada)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao
            else:
                break
        case 6:
            macarronada = codigo_card(opcao)
            carrinho_de_compra.append(macarronada)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao
            else:
                break
        case 7:
            bebidas = codigo_card(opcao)
            carrinho_de_compra.append(bebidas)
            opcao2=int(input("""Deseja adcionar outro prato ?
                          1- SIM
                          0- NÂO
                         : """))
            if opcao2==1:
                opcao
            else:
                break

#Formas de pagamento        
while True:
    opcao3 = int(input(""" ==== PAGAMENTO ====
                   1- DEBITO
                   2- CRÉDITO
                   3- DINHEIRO
                   4- PIX
                   : """)) 
    while True:
        if (opcao >=1) and (opcao <=4):
                break
        else:
            print("Favor selecionar uma opção valida.")
            time.sleep(2)
    match (opcao3):
        case 1:
            total = sum(carrinho_de_compra)
            valor_total, desconto = finalizando_compra(opcao3,carrinho_de_compra)
            print("Pagamento: Débito")
            print(f"Valor Bruto: {total:.2f}R$")
            print(f"Desconto: {desconto:.2f}R$")
            print(f"Valor com desconto: {valor_total:.2f}R$")
            print(f"Codigo dos produtos solicitados: {lista_selecao}")
            break
        case 2:
            total = sum(carrinho_de_compra)
            valor_total, desconto = finalizando_compra(opcao3,carrinho_de_compra)
            print("Pagamento: Crédito")
            print(f"Valor Bruto: {total:.2f}R$")
            print(f"Acréscimo: {desconto:.2f}R$")
            print(f"Valor acrescido: {valor_total:.2f}R$")
            print(f"Codigo dos produtos solicitados: {lista_selecao}")
            break
        case 3:
            total = sum(carrinho_de_compra)
            valor_total, desconto = finalizando_compra(opcao3,carrinho_de_compra)
            print("Pagamento: Dinheiro")
            print(f"Valor Bruto: {total:.2f}R$")
            print(f"Desconto: {desconto:.2f}R$")
            print(f"Valor com desconto: {valor_total:.2f}R$")
            print(f"Codigo dos produtos solicitados: {lista_selecao}")
            break
        case 4:
            total = sum(carrinho_de_compra)
            valor_total, desconto = finalizando_compra(opcao3,carrinho_de_compra)
            print("Pagamento: Pix")
            print(f"Valor Bruto: {total:.2f}R$")
            print(f"Desconto: {desconto:.2f}R$")
            print(f"Valor com desconto: {valor_total:.2f}R$")
            print(f"Codigo dos produtos solicitados: {lista_selecao}")
            break
 