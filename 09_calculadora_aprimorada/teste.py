
def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 == 0:
        return "Erro: não é possível dividir por zero."
    return numero1 / numero2


def exibir_resultado(resultado):
    if isinstance(resultado, (int, float)):
        if resultado.is_integer() if isinstance(resultado, float) else True:
            print(f"Resultado: {int(resultado)}")
        else:
            print(f"Resultado: {resultado:.2f}")
    else:
        print(resultado)


def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        operacao = input("\nEscolha uma operação: ")

        if operacao == "0":
            print("Calculadora encerrada. Até mais!")
            break

        if operacao not in ["1", "2", "3", "4"]:
            print("Operação inválida! Tente novamente.")
            continue

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if operacao == "1":
                resultado = somar(numero1, numero2)

            elif operacao == "2":
                resultado = subtrair(numero1, numero2)

            elif operacao == "3":
                resultado = multiplicar(numero1, numero2)

            elif operacao == "4":
                resultado = dividir(numero1, numero2)

            exibir_resultado(resultado)

        except ValueError:
            print("Erro: digite apenas números válidos.")


calculadora()
