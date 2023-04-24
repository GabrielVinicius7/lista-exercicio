

try:
    str1 = str(input('adicione uma frase:'))
    str2 = str(input('adicione outra frase:'))

    if len(str2) != len(str1):
        raise Exception ('Não tem o mesmo tamanho!')
except Exception as e:
    print(e)
else:
    print('Ok as frases tem o mesmo tamanho!')