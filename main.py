#funções
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

#progama principal
if __name__ == '__main__':
    try:
        n = int(input('Informe um numero inteiro positivo: '))

        if n >= 0:
            print(f'O fatorla de {n} = {fatorial(n)}.')
        else:
            print(f'Não foi possivel calcular o fatorial de {n}')
    except:
        print('Não foi possicel calcular o fatorial.')