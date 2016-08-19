from models import *
arquivo = None
try:
    arquivo = open('srsr.txt')
    print('arquivo foi aberto')
    arquivo.close()
except (IOError, TypeError) as erro:
    print('Deu Error %s' % erro)
finally:
    if(arquivo is not None):
        arquivo.close()


try:
    with open('perfis.csv', 'r') as arquivo
        for linhas in arquivo:

except IOError as erro:
