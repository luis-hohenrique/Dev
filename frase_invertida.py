frase = input('Escreva uma frase: ')
print(' Frase Original: {}'.format(frase))
inversao = ' '.join(palavra[::-1] for palavra in frase.split())
print('Frase invertida: {}'.format(inversao))