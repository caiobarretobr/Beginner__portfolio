from functions import *
import sys

def main():
    # Menu com opções: calcular, ver histórico, limpar histórico, sair
    # Cada operação em uma função separada
    # Divisão por zero e entrada inválida (texto no lugar de número) não podem quebrar o programa
    # O histórico mostra as últimas 10 contas numeradas

    while True:
        print("Escolha as opções abaixo")
        print("------------------------")
        print("1 - Calcular")
        print("2 - Ver histórico")
        print("3 - Limpar histórico")
        print("4 - Sair")

        answer = int(input("Sua resposta: "))

        match answer:
            case 1:
                calc()
            case 2:
                history()
            case 3:
                clean()
            case 4:
                print("Saindo...")
                sys.exit()
            case _:
                print("Digite uma opção válida.")

    while True: 
        n1 = int(input("Digite o 1o Número: "))
        n2 = int(input("Digite o 2o Número: "))
        op = input("Insira a operação: ")

        match op:
            case "+":
                print(f"Resultado: {n1 + n2}")
            case "-":
                print(f"Resultado: {n1 - n2}")
            case "*":
                print(f"Resultado: {n1 * n2}")
            case "/":
                print(f"Resultado: {n1 / n2}")
            case "**":
                print(f"Resultado: {n1 ** n2}")
            case _:
                "Operação inválida"

        if input("Continuar? s/n ") == "n":
            break


if __name__ == "__main__":
    main() 