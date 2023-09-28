#TESTE CÓDIGO PYTHON PARA ABASTECER COM ALCOOL OU GASOLINA WJUNIOR

print("Bem vindo ao posto WJUNIOR") #Escreva
print("Escolha o tipo de combustível:") #Escreva
print("1. Álcool") #Escreva
print("2. Gasolina") #Escreva

combustivel = int(input("Digite o número que corresponde ao combustível : "))

preco_alcool = 4.50  
preco_gasolina = 6.20  

litros_abastecidos = int(input("Quantos litros você deseja abastecer? "))

if combustivel == 1:
    preco_total = litros_abastecidos * preco_alcool
    tipo_combustivel = "Álcool"

elif combustivel == 2:
    preco_total = litros_abastecidos * preco_gasolina
    tipo_combustivel = "Gasolina"

else:
    print("Escolha inválida. Por favor, escolha 1 para Álcool ou 2 para Gasolina.")
    preco_total = 0

if preco_total > 0:
    print(f"Você abasteceu {litros_abastecidos:} litros de {tipo_combustivel} e o valor total a ser pago é R${preco_total:}.")

else:
    print("Operação de abastecimento cancelada.")
