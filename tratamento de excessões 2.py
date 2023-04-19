
try:
    string = str(input('Apenas letras maiusculas :'))
    if string != string.upper():
        raise Exception('MINÚSCULA!')
except Exception as a:
    print(a)

else:
    print('Ok, Apenas letra certas!')


