import random
print('''       Funções
Escolha sua função:
    - Inverter string (1)
    - Ordenar caracteres da string (2)
    - Retornar dia da semana para data (3)
    - Detectar palíndromos (4)
    - Retornar número par ou ímpar (5)
    - Sortear um número aleátorio com intervalo (6)
    - Verificar se palavra ou caracter existe em string (7)
    - Imprimir o número Pi com x casas decimais (8)''')
func = int(input(''))
if func == 1:
    str = input('Digite sua string --> ')
    inv = str [::-1]
    print('String invertida:', inv)
elif func == 4:
    pal = input("Digite sua palavra --> ")
    if pal == pal [::-1]:
        print('Sua palavra é um palíndromo!!')
    else: 
        print('Sua palavra não é um palíndromo :c')
elif func == 5:
    num = int(input('Digite seu número --> '))
    if num % 2 == 0:
        print('Seu número é par!')
    elif num % 2 == 1:
        print('Seu númeor é ímpar :( :(')
    else: 
        print('Seu número não existe, ele é falso')
elif func == 6:
    num = random.randint(int(input('Digite o ínico do intervalo --> ')),int(input('Digite o fim do intervalo --> ')))
    print('O número sorteado foi %d !!!' % num)