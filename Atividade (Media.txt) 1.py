
n = open('armazenamento.txt','w')

armazem = []


while True:

    nome = (input('Nome:'))
    n1 = float(input('1° Nota:'))
    n2 = float(input('2° Nota:'))
    n3 = float(input('3° Nota:'))
    n.write(f"{nome},{n1},{n2},{n3}\n")

    question = str(input('Quer continuar? [S/N]')).upper().split()[0]

    if question == 'N':
        break
    if question != 'N' and question != 'S':
        break





