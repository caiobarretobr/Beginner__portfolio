import time
from pathlib import Path
from collections import deque

# 1 - CALC()

#   FAZ UMA OPERAÇÃO
#   MOSTRA NA TELA
#   ARMAZENA EM UM ARQUIVO "HISTORY.TXT"

# 2 - HISTORY()

#   MOSTRAR ÚLTIMAS 10 LINHAS DO ARQUIVO "HISTORY.TXT"

# 3 - CLEAN()
# 
#   LIMPAR O ARQUIVO "HISTORY.TXT"

FOLDER = Path(__file__).resolve().parent
DIRECTORY = FOLDER / "history.txt"

def calc():
    def store(calc):
        print(calc)

        with open(DIRECTORY, "a", encoding="utf-8") as file:
            file.write(f"{calc}\n")

    while True:
        n1 = input("Digite o 1o Número: ")

        if n1.isdigit():
            n1 = float(n1)
            break
        else:
            print("Digite um número.")
            time.sleep(0.5)
            print("\n")

    while True:
        n2 = input("Digite o 2o Número: ")

        if n2.isdigit():
            n2 = float(n2)
            break
        else:
            print("Digite um número")
            time.sleep(0.8)
            print("\n")

    while True:
        op = input("Digite a operação: ")

        if op == "+" or op == "-" or op == "*" or op == "/" or op == "**":
            break
        else:
            print("Digite um operador válido")
            time.sleep(0.8)
            print("\n")

    if n1 == 0 and n2 == 0 and op == "/":
        print("ERRO: Operação inválida")
        time.sleep(0.8)
        print("\n")
    else:
        match op:
            case "+":
                calc = f"{n1} + {n2} = {n1 + n2}"
                store(calc)
                time.sleep(0.9)
                print("\n")
            case "-":
                calc = f"{n1} - {n2} = {n1 - n2}"
                store(calc)
                time.sleep(0.9)
                print("\n")
            case "*":
                calc = f"{n1} * {n2} = {n1 * n2}"
                store(calc)
                time.sleep(0.9)
                print("\n")
            case "/":
                calc = f"{n1} / {n2} = {n1 / n2:.2f}"
                store(calc)
                time.sleep(0.9)
                print("\n")
            case "**":
                calc = f"{n1} ** {n2} = {n1 ** n2}"
                store(calc)
                time.sleep(0.9)
                print("\n")
            case _:
                "Operação inválida"

def history():

    with open(DIRECTORY, "a", encoding="utf-8") as file:
        with open(DIRECTORY, "r", encoding="utf-8") as file:
            if DIRECTORY.stat().st_size == 0:
                print("Não há histórico disponível.")
            else:
                lines = deque(file, maxlen=10)

                for line in lines:
                    print(line.strip())

    time.sleep(0.9)
    print("\n")

def clean():
    with open(DIRECTORY, "a", encoding="utf-8") as file:

        if DIRECTORY.stat().st_size == 0:
            print("Não existe histórico pra deletar.")
            time.sleep(0.9)
            print("\n")
        else:
            with open(DIRECTORY, "w", encoding="utf-8") as file:
                pass
            print("Histórico Limpo!")
            time.sleep(0.9)