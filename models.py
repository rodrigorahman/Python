#-*- coding: UTF-8 -*-

class Perfil(object):

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print "Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def imprimir_curtidas(self):
        print self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise ArgumentoInvalidoError('uma linha no arquivo %s deve ter 3 valores', % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis

class Data(object):

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print "%s/%s/%s" % (self.dia,self.mes,self.ano)


class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime_imc(self):
        altura_imc = self.altura * self.altura
        imc = self.peso / altura_imc
        print "Imc de Ronald: %s" % (imc)


class Perfil_Vip(Perfil):

    def __init__(self,nome,telefone,empresa, apelido=''):
        super(Perfil_Vip,self).__init__(nome,telefone,empresa)
        self.apelido = apelido


class ArgumentoInvalidoError(Exception):

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)
