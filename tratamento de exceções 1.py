# Número inteiro

n = int(input('Digite um número inteiro :'))

try:
    if n % 2==1:
       raise Exception ('OK, impar!')
except Exception as a:
     print(a)
else:
    print('OK, PAR!')

