

minimo = 1320


# Coletando informações

horas = float(input('Quantidade de horas trabalhadas :'))
turno = str(input(' (M) Matutino\n (V) Vespertino\n (N) Noturno \nQual turno de trabalho : '))
categoria = str(input(' (G) Gerente \n (O)Operário \nQual categoria :'))

# Aplicando as condições necessarias

if categoria in 'Gg' and turno in 'Mm'or turno in 'Vv':
    porcento15 = ((minimo*15)/100)*horas
    print('Sálario R${:.2f} '.format(porcento15))
elif categoria in 'Gg' and turno in 'Nn':
    porcento10 = ((minimo*10)/100)*horas
    print('Sálario R${:.2f} '.format(porcento10))
elif categoria in 'Oo' and turno in 'Nn':
    porcento9 = ((minimo*9)/100)*horas
    print('Sálario R${:.2f} '.format(porcento9))
elif categoria in 'Oo' and turno in 'Mm' or turno in 'Vv':
    porcento14 = ((minimo*14)/100)*horas
else:
    print('\033[31mINEXISTENTE!!\033[m')




