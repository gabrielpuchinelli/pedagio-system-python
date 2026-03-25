tipo_veiculo = input("Digite o tipo de veículo(carro, moto, caminhão ou oficial): ")
hora_passagem = int(input("Digite a hora da passagem: "))

if tipo_veiculo == "oficial":
    valor_final = 0
else:

    if tipo_veiculo == "carro":
        valor_base = 10
    elif tipo_veiculo == "caminhao":
        valor_base = 15
        eixos = int(input("Digite a quantidade de eixos: "))
        valor_base = 15 * eixos
    elif tipo_veiculo == "moto":
        valor_base = 5

    if (hora_passagem >= 6 and hora_passagem <= 9) or (hora_passagem >= 17 and hora_passagem <= 20):
        valor_final = valor_base * 1.20
    else:
        valor_final = valor_base

print("Tipo de veículo:", tipo_veiculo)
print("Valor final:", valor_final)
