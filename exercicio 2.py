# ELEVADORES

fim = str(input('Olá,poderia ajudar neste questionario? [S]/[N]:')).upper()

#abaixo, iniciando variaveis para descobrir o valor das opcoes do elevador
elev1 = elev2 = elev3 = 0
#abaixo, iniciando variaveis para descobrir o valor das opcoes do periodo
m1 = v1 = no1 = 0

percentual = 0



while "N" not in fim:

    # Coletando informações sobre os elevadores

    n1 = str(input('Qual é o elevador mais utilizado : \n[A]\n[B]\n[C]')).upper()
    if n1 =="A":
        elev1 += 1
    elif n1 == "B":
        elev2 += 1
    elif n1 == "C":
        elev3 += 1
    else:
        n1 = str(input('Elevador não encontrado!, entre os três qual ? : \n[A]\n[B]\n[C]')).upper()

    # Coletando informações sobre os Periodos.

    n2 = str(input('Período mais utilizado: \n[M]Matutino\n[V]Vespertino\n[N]Noturno')).upper()[0]
    if n2 == "M":
        m1 += 1
    elif n2 == "V":
        v1 += 1
    elif n2 == "N":
        no1 += 1
    else:
        n1 = str(input('Elevador não encontrado!, entre os três qual ? : \n[A]\n[B]\n[C]')).upper()
    percentual += 1
    fim = str(input('Continuar ? [S]/[N]')).upper()

# Descobrindo o elevador mais utilizado

if elev1 > elev2 and elev1 > elev3:
    mais1 = elev1
    print("O elevador mais utilizado é o [A] , usado {} vezes".format(mais1))
if elev2 > elev1 and elev2 > elev3:
    mais1 = elev2
    print( 'O elevador mais utilizado é o [B], usado {} vezes'.format(mais1))
elif elev3 > elev1 and elev3 > elev2:
    mais1 = elev3
    print( 'O elevador mais utilizado é o [C], usado {} vezes'.format(mais1))

# Descobrindo o periodo mais utilizado

if m1 > v1 and m1 > no1:
    mais = m1
    print("O Periodo mais utilizado é o [M] Matutino, usado {} vezes".format(mais))
if v1 > m1 and v1 > no1:
    mais = v1
    print( 'O Periodo mais utilizado é o [V] Vespertino, usado {} vezes'.format(mais))
elif no1 > m1 and no1 > v1:
    mais = no1
    print( 'O Periodo mais utilizado é o [N] Noturno, usado {} vezes'.format(mais))

# Descobrindo o periodo menos utilizado.

if m1 < v1 and m1 < no1:
    menos = m1
    print("O Periodo menos utilizado é o [M] Matutino, usado {} vezes".format(menos))
if v1 < m1 and v1 < no1:
    menos = v1
    print( 'O Periodo menos utilizado é o [V] Vespertino, usado {} vezes'.format(menos))
elif no1 < m1 and no1 < v1:
    menos = no1
    print( 'O Periodo menos utilizado é o [N] Noturno, usado {} vezes'.format(menos))

#Calculando porcentual entre os periodo mais e menos utilizados.

maior_percentual = ((mais * 100)/percentual)
menor_percentual = ((menos * 100)/percentual)

total_percentual = (maior_percentual-menor_percentual)
print('A diferença porcentual entre o mais o usado periodos e o menos usados é de {:.0f}%.'.format(total_percentual))


