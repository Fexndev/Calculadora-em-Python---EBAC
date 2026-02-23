#!/bin/bash
# calculadora.sh — calculadora simples (soma, subtração, multiplicação, divisão)

echo "=== Calculadora (Bash) ==="
read -p "Digite o 1º número: " n1
read -p "Digite o 2º número: " n2

echo "Escolha a operação:"
echo "  1) Soma (+)"
echo "  2) Subtração (-)"
echo "  3) Multiplicação (*)"
echo "  4) Divisão (/)"
read -p "Opção (1-4): " op

case "$op" in
  1) result=$(echo "$n1 + $n2" | bc) ;;
  2) result=$(echo "$n1 - $n2" | bc) ;;
  3) result=$(echo "$n1 * $n2" | bc) ;;
  4)
     if [ "$(echo "$n2 == 0" | bc)" -eq 1 ]; then
       echo "Erro: divisão por zero."
       exit 1
     fi
     # scale define casas decimais
     result=$(echo "scale=4; $n1 / $n2" | bc)
     ;;
  *) echo "Opção inválida." ; exit 1 ;;
esac

echo "Resultado: $result"
