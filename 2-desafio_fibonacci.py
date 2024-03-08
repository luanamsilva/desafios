# Desafio -2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci_sequence(n):
    sequence = [0, 1]

    while sequence[-1] < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

def check_fibonacci(num, sequence):
    if num in sequence:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."

def main():
     while True:
        try:
            choice = int(input("Digite 1 para verificar se um número pertence à sequência de Fibonacci ou 2 para sair: "))
            
            if choice == 2:
                print("Programa encerrado.")
                break
            elif choice == 1:
                num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
                fib_sequence = fibonacci_sequence(num)
                print(check_fibonacci(num, fib_sequence))
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")
        
        except ValueError:
            print("Por favor, insira um número válido.") 

main()
