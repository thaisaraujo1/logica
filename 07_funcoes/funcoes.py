#Função sem retorno e sem parâmetro
def sobre():
    print("Desenvolvido por: Thais Araujo")

#Função sem re torno e com parâametros
def turma(turma, ano):
    print(f"Turma: {turma} - {ano}")

    # Função com retorno e com parâmetros
def somar(numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD-05", 2026)

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

resultado = somar(10, 5)
print (f"A soma de 10 + 5 = {resultado}")
