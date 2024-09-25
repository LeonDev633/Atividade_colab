#verificar se o pagamento sera a vista ou por credito ou debito
#O sistema deve solicitar a forma de pagamento:
#À vista (desconto de 10% sobre o valor total).
#Cartão de crédito (acréscimo de 10% sobre o valor total).

valores = []
valor_total = valores

def debito_credito(pagamento):
    match(pagamento):
        case "debito":
            pagamento_final = valor_total * 10
        case "credito":
            print("teste")