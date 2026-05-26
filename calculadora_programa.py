import operacoes

print('calculadora'.upper().center(50,'='))

ops = ['soma', 'subtração', 'multiplicação', 'divisão']

for i in range(len(ops)):
    print(f'[{i}] {ops[i]}')

n1 = input('digite o primeiro número: ')
n2 = input('digite o segundo número: ')
operacao = input('digite a operação: ')

match operacao:
    case 0:
        print(f'a soma é {operacoes.soma(n1,n2)}')
    case 1:
        print(f'a subtração é {operacoes.subtração(n1,n2)}')
    case 2:
        print(f'a multiplicação é {operacoes.multiplicação(n1,n2)}')
    case 3:
        print(f'a divisão é {operacoes.divisão(n1,n2)}')
    case _:
        print('escolha inválida!')
