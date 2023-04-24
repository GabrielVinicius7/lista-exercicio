n = open('armazenamento.txt', 'r')

armazem = n.read()

nomes = []
notas = []
cont = 0



#print(armazem.split(','))



for cada in armazem.split(";"):
    cont += 1
    c = cada.split(",")
    print(c)


    nome = (cada[0])
    print(nome)
    n1 = (cada[1])
    n2 = (cada[2])
    n3 = (cada[3].strip())




    notas.append([n1,n2,n3])
    nomes.append(nome)

    print(type(n1))
    for a in range(cont):
        nome = nome[a]
        nota1, nota2, nota3 = notas[a]
        media = float((nota1 + nota2 + nota3) / 3)



        print(media)





















