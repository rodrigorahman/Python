## Python ##

Rodando um arquivo Python

```

```
## Setando enconding ##

***Indicando o interpretador Python que deve rodar o arquivo como utf-8***
```
# -*- coding: UTF-8 -*-
```


## Atributos privados ##


Declarar com __ ex:
```
class Perfil(object):

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print "Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)

```

O Python troca o __ do atributo por um valor aleatorio que não conseguimos saber assim é a unica forma que podemos colocar um atributo privado


## Leitura de Arquivo ##

```
arquivo = open('perfil.csv', 'r')
linha = arquivo.readLine()

for linha in arquivo:
  print linha

arquivo.close()
```

## Escrevendo no arquivo ##

```
arquivo = open('arquivo_novo.csv', 'w')
arquivo.write('Pedro Gomes, 2344444, Gomes e amigos \n')
arquivo.close()
```


***passando a inves de w o python apenda no arquivo***

a - acrescenta no final do arquivo

w - sempre escreve no inicio do arquivo, conteúdo existente será apagado


## Metodos staticos ##

Para metodo estatico colocar o modificador @staticmethod

Para criar um metodo generico de classe utilizar @classmethod ex:

```
@classmethod
def gerar_perfis(classe, nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    perfis = []
    for linha in arquivo
        valores = linha.split(',')
        perfis.append(classe(*valores))
    arquivo.close()
    return perfis
```

## Valores defaults ##

Caso queira deixar um valor padrão em um metodo basta adicionad =<valor> ex:

```
def __init__(self,nome,telefone,empresa, apelido=''):
```

Apelido não é obrigatorio


## Estudar ##

Parametro with ex:

```
with open('perfis.csv', 'r') as arquivo
      for linhas in arquivo:
```

## PIP ##

Gerenciado de dependencias Python

Quando der problema de instalação devido a uma versao pré instalada basta adicionar o parametro

***--ignore-installed***
