"""Exibir um menu com 7 pratos, apresentando o código do prato e o nome.
O usuário poderá inserir o código do prato desejado. Caso o código seja inválido, o sistema deve alertar o usuário e pedir novamente um código válido.
O sistema deverá perguntar ao usuário se ele deseja fazer outro pedido e, se sim, permitir a adição de mais pratos ao pedido.
Acumular os valores de cada prato escolhido.
Se o usuário digitar o código "0", o programa encerrará o pedido e calculará o valor total.
O sistema deve solicitar a forma de pagamento:
À vista (desconto de 10% sobre o valor total).
Cartão de crédito (acréscimo de 10% sobre o valor total).
Exibir os resultados ao final:
A lista com os códigos e nomes dos pratos escolhidos.
O subtotal (valor total sem acréscimo ou desconto).
A forma de pagamento escolhida.
O valor do desconto ou acréscimo aplicado.
O valor final a ser pago."""

import os
os.system("cls||clear")

print(""" 
escreva o codigo do prato para fazer o pedido:
codigo |alimento       |valor |
1      |picanha        |25,00 |
2      |lasanha        |20,00 |
3      |strogonoff     |180,00|
4      |bife acebolado |15,00 |
5      |bife acebolado |15,00 |
6      |bife acebolado |15,00 |
7      |bife acebolado |15,00 |
    """)
while True:
    opcao = input("escolha seu prato:")
    match(opcao):
        case "1":
            pedido = "picanha $25,00"
            opc = int(input)
            if opc == 1:
                break
        case "2":
            pedido = "lasanha $20,00"
        case "3":
            pedido = "strogonoff $180,00"
        case "4":
            pedido = "bife acebolado $15,00"
        case _:
            print("não consta no menu")

print(f"Pedido escolhido e suas informações: {pedido}")