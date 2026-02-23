#!/usr/bin/env python3
# calculadora.py — calculadora simples (soma, subtração, multiplicação, divisão)

def read_number(label: str) -> float:
    while True:
        raw = input(label).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 10 ou 10.5).")


def main() -> None:
    print("=== Calculadora (Python) ===")
    n1 = read_number("Digite o 1º número: ")
    n2 = read_number("Digite o 2º número: ")

    print("Escolha a operação:")
    print("  1) Soma (+)")
    print("  2) Subtração (-)")
    print("  3) Multiplicação (*)")
    print("  4) Divisão (/)")

    op = input("Opção (1-4): ").strip()

    if op == "1":
        result = n1 + n2
    elif op == "2":
        result = n1 - n2
    elif op == "3":
        result = n1 * n2
    elif op == "4":
        if n2 == 0:
            print("Erro: divisão por zero.")
            return
        result = n1 / n2
    else:
        print("Opção inválida.")
        return

    # Mostra inteiro sem .0 quando couber, senão mostra com até 4 casas
    if float(result).is_integer():
        print(f"Resultado: {int(result)}")
    else:
        print(f"Resultado: {result:.4f}")


if __name__ == "__main__":
    main()
