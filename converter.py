def decimal_to_binario(dec):
    # Converte decimal para binário e preenche com zeros à esquerda
    binario = bin(dec)[2::]
    return binario.zfill(11)


def binario_to_decimal(binario):
    # Converte binário para decimal
    dec = int(binario, 2)
    return dec


def decimal_to_octal(dec):
    # Converte decimal para octal e preenche com zeros à esquerda
    octal = oct(dec)[2:]
    return octal.zfill(4)


def decimal_to_hexadecimal(dec):
    # Converte decimal para hexadecimal e preenche com zeros à esquerda
    hexadecimal = hex(dec)[2:]
    return hexadecimal.zfill(3)


def soma_bin(bin1, bin2):
    # Soma binários
    carry = 0
    resultado = ''
    for i in range(10, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_ = bit1 + bit2 + carry
        carry = sum_ // 2
        resultado = str(sum_ % 2) + resultado
    return resultado


def main():
    try:
        # Entrada do usuário
        V1 = int(input("Digite um número inteiro: "))
        V2 = int(input("Digite outro número inteiro: "))
        base_saida = int(input("Digite 10 para Decimal, 2 para Binário, 8 para Octal e 16 para Hexadecimal: "))

        # Restrições
        if not (0 <= V1 <= 512 or 0 <= V2 <= 512):
            print("ERRO: Os números devem estar entre 0 e 512.")
            exit()

        if base_saida not in [2, 8, 10, 16]:
            print("ERRO: A base de saída deve ser 2, 8, 10 ou 16.")
            exit()

        # Lógica principal
        if base_saida == 10:
            result = str(V1 + V2)
        elif base_saida == 2:
            binario1 = decimal_to_binario(V1)
            binario2 = decimal_to_binario(V2)
            result = soma_bin(binario1, binario2)
        elif base_saida == 8:
            result = decimal_to_octal(V1 + V2)
        elif base_saida == 16:
            result = decimal_to_hexadecimal(V1 + V2)
        else:
            print("ERRO")
            exit()

        # Resultado
        print("Resultado:", result)

    except ValueError:
        print("ERRO: Entrada inválida. Certifique-se de digitar números inteiros.")
        exit()


main()
