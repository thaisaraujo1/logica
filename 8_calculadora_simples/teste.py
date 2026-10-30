
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = primeiro_numero + segundo_numero

elif operador == "-":
    resultado = primeiro_numero - segundo_numero

elif operador == "*":
    resultado = primeiro_numero * segundo_numero

elif operador == "/":
    if segundo_numero == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = primeiro_numero / segundo_numero

else:
    print("Operador inválido")

# Formatação do resultado
if operador in ["+", "-", "*", "/"] and not (operador == "/" and segundo_numero == 0):
    if resultado.is_integer():
        print(int(resultado))
    else:
        print(round(resultado, 2))
