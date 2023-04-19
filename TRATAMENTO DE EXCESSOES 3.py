
try:
    n = int(input('Digite um número inteiro:'))
    a = 10/n
except ZeroDivisionError:
     print('ERRO! FINALIZANDO!')
else:
    print(f'A divisão é igual há {a}')
