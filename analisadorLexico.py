from typing import Deque, Any
from collections import deque


class fila():
    def __init__(self):
        self.arquivoTxt = open('./lerarquivo.txt', 'r')

    def inserirOsElementosNaFila(self):
        queue: Deque[Any] = deque()
        for leituraArquivo in self.arquivoTxt:
            queue.append(leituraArquivo)
        return queue


class tabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.error = {}

    def adicionarSimbolo(self, lexema, token, tipo):
        if not self.verificarSimboloExistente(lexema):
            self.simbolos[lexema] = {"Classe": lexema, "Token": token, "Tipo": tipo}

    def adicionarErro(self, lexema, token, tipo):
        if not self.verificarErroExistente(lexema):
            self.error[lexema] = {"Classe": lexema, "Token": token, "Tipo": tipo}

    def verificarSimboloExistente(self, lexema):
        return lexema in self.simbolos

    def verificarErroExistente(self, lexema):
        return lexema in self.simbolos

    def retornarValorDaTabelaDeSimbolos(self, lexema):
        if lexema in self.simbolos:
            return self.simbolos.get(lexema)


class analisadorLexico:
    def __init__(self):
        self.tabelaDeSimbolos = tabelaDeSimbolos()
        self.analisador = ''
        self.classificador = ''
        self.simbolosAnalisados = []
        self.classificarNumber = 0
        self.lexema = ''
        self.coluna = 0
        self.linha = 0
        self.queue: Deque[Any] = deque()

    def iniciarTabelaDeSimbolos(self):
        self.tabelaDeSimbolos.adicionarSimbolo("inicio", "inicio", "")
        self.tabelaDeSimbolos.adicionarSimbolo("varinicio", "varinicio", "")
        self.tabelaDeSimbolos.adicionarSimbolo("varfim", "varfim", "")
        self.tabelaDeSimbolos.adicionarSimbolo("escreva", "escreva", "")
        self.tabelaDeSimbolos.adicionarSimbolo("leia", "leia", "")
        self.tabelaDeSimbolos.adicionarSimbolo("se", "se", "")
        self.tabelaDeSimbolos.adicionarSimbolo("entao", "entao", "")
        self.tabelaDeSimbolos.adicionarSimbolo("fimse", "fimse", "")
        self.tabelaDeSimbolos.adicionarSimbolo("fim", "fim", "")
        self.tabelaDeSimbolos.adicionarSimbolo("facaAte", "facaAte", "")
        self.tabelaDeSimbolos.adicionarSimbolo("fimFaca", "fimFaca", "")
        self.tabelaDeSimbolos.adicionarSimbolo("inteiro", "inteiro", "int")
        self.tabelaDeSimbolos.adicionarSimbolo("lit", "lit", "literal")
        self.tabelaDeSimbolos.adicionarSimbolo("real", "real", "double")

    def adicaoDeSimbolosLidos(self, lexema, linha, coluna):
        simbolo = self.tabelaDeSimbolos.simbolos[lexema]
        simbolo["Linha"] = linha
        simbolo["Coluna"] = coluna
        self.simbolosAnalisados.append(simbolo.copy())

    def adicaoDeErrosLidos(self, lexema, linha, coluna):
        simbolo = self.tabelaDeSimbolos.error[lexema]
        simbolo["Linha"] = linha
        simbolo["Coluna"] = coluna
        self.simbolosAnalisados.append(simbolo.copy())


    def lexico(self):
        self.pegarFila = fila().inserirOsElementosNaFila()
        self.iniciarTabelaDeSimbolos()
        for caracter in self.pegarFila:
            self.linha += 1
            self.coluna = 0
            self.estadoAtual = 's0'
            for k in caracter:
                self.coluna += 1
                self.estadoAtual = self.mudandoOEstadoConformeLeitura(k, self.estadoAtual)
                if self.estadoAtual == 's1' or self.estadoAtual == 's2':
                    self.lexema = self.lexema + k
                    self.classificador = self.realizacaoDeClassificacao(k)
                elif self.estadoAtual == 's3' or self.estadoAtual == 's4':
                    continue
                elif self.estadoAtual == 's5':
                    self.lexema = self.lexema + k
                    self.classificador = self.realizacaoDeClassificacao(k)
                elif self.estadoAtual == 's6':
                    self.estadoAtual = self.mudandoOEstadoConformeLeitura(caracter.__getitem__(self.coluna), self.estadoAtual)
                    if self.estadoAtual == 's7':
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = k
                    elif self.estadoAtual == 's8':
                        if self.lexema != '':
                            self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                            self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                            self.lexema = k
                        elif k != '':
                            self.lexema = k
                    elif self.estadoAtual == 's9':
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = k
                    else:
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's7':
                    self.estadoAtual = self.mudandoOEstadoConformeLeitura(caracter.__getitem__(self.coluna), self.estadoAtual)
                    if self.estadoAtual == 's6':
                        self.lexema = self.lexema + k
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                        self.lexema = ''
                    elif self.estadoAtual == 's8':
                        if self.lexema != '':
                            self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                            self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                            self.lexema = k
                        elif k != '':
                            self.lexema = k
                    else:
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, k)
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's8':
                    self.estadoAtual = self.mudandoOEstadoConformeLeitura(caracter.__getitem__(self.coluna-2), self.estadoAtual)
                    if self.estadoAtual == 's6' or self.estadoAtual == 's7':
                        self.lexema = self.lexema + k
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, self.lexema)
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna)
                        self.lexema = ''
                    else:
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's10':
                    if self.lexema == '<':
                        self.lexema = self.lexema + k
                        self.classificador = self.realizacaoDeClassificacao(self.lexema)
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '=')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna)
                        self.lexema = ''
                    else:
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, k)
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's11':
                    if self.lexema != '':
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                    elif k != '':
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's12':
                    if self.validarInteiroOuFloat(self.lexema) == 0 and self.realizacaoDeClassificacao(self.lexema) == 'num':
                        self.classificarNumber = 'double'
                    elif self.validarInteiroOuFloat(self.lexema) == 1 and self.realizacaoDeClassificacao(self.lexema) == 'num':
                        self.classificarNumber = 'int'
                    else:
                        self.classificarNumber = ''
                    if self.lexema != '':
                        self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, self.classificarNumber)
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                    elif k != '':
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's13':
                    if self.tabelaDeSimbolos.verificarSimboloExistente(self.lexema):
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                        self.lexema = ''
                        self.classificador = self.realizacaoDeClassificacao(k)
                        self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                        self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                    else:
                        if self.validarInteiroOuFloat(self.lexema) == 0 and self.classificador == 'num':
                            self.classificarNumber = 'double'
                        elif self.validarInteiroOuFloat(self.lexema) == 1 and self.realizacaoDeClassificacao(self.lexema) == 'num':
                            self.classificarNumber = 'int'
                        else:
                            self.classificarNumber = ''
                        if self.lexema != '':
                            self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, self.classificarNumber)
                            self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna - 1)
                            self.lexema = ''
                            self.classificador = self.realizacaoDeClassificacao(k)
                            self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                            self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                        elif k != '':
                            self.classificador = self.realizacaoDeClassificacao(k)
                            self.tabelaDeSimbolos.adicionarSimbolo(k, self.classificador, '')
                            self.adicaoDeSimbolosLidos(k, self.linha, self.coluna)
                elif self.estadoAtual == 's16':
                    if self.tabelaDeSimbolos.verificarSimboloExistente(self.lexema):
                        self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna)
                        self.lexema = ''
                    else:
                        if self.lexema != '':
                            self.tabelaDeSimbolos.adicionarSimbolo(self.lexema, self.classificador, '')
                            self.adicaoDeSimbolosLidos(self.lexema, self.linha, self.coluna)
                            self.lexema = ''
                elif self.estadoAtual == 's17':
                    self.classificador = self.realizacaoDeClassificacao(k)
                    self.tabelaDeSimbolos.adicionarErro(k, self.classificador, '')
                    self.adicaoDeErrosLidos(k, self.linha, self.coluna)
        self.coluna = 1
        self.tabelaDeSimbolos.adicionarSimbolo('', '$', '')
        self.adicaoDeSimbolosLidos(self.lexema, self.linha+1, self.coluna)

    def validarInteiroOuFloat(self, number):
        try: 
            int(number)
            return 1
        except ValueError:
            return 0



    def realizacaoDeClassificacao(self, analysis):
        switcher = {
            # SimbolosGerais
            '"': 'Literal', '{': 'Comment', '}': 'Comment', '<': 'OPR', '>': 'OPR', '=': 'OPR', '<-': 'RCB',
            '+': 'OPM', '-': 'OPM', '*': 'OPM', '/': 'OPM', '(': 'AB_P', ')': 'FC_P', ';': 'PT_V', ',': 'VIR',
            'EOF': 'EOF', "\n": '', " ": '', '<>': 'OPR', '>=': 'OPR', '<=': 'OPR',
            # SimbolosDeNumeros
            '0': 'num', '1': 'num', '2': 'num', '3': 'num', '4': 'num', '5': 'num', '6': 'num',
            '7': 'num', '8': 'num', '9': 'num', '.': 'num',
            # SimbolosDeLetras
            'a': 'id', 'b': 'id', 'c': 'id', 'd': 'id', 'e': 'id', 'f': 'id', 'g': 'id', 'h': 'id', 'i': 'id',
            'j': 'id', 'k': 'id', 'l': 'id', 'm': 'id', 'n': 'id', 'o': 'id', 'p': 'id', 'q': 'id', 'r': 'id',
            's': 'id', 't': 'id', 'u': 'id', 'v': 'id', 'x': 'id', 'y': 'id', 'z': 'id', 'A': 'id', 'B': 'id',
            'C': 'id', 'D': 'id', 'E': 'id', 'F': 'id', 'G': 'id', 'H': 'id', 'I': 'id', 'J': 'id', 'K': 'id',
            'L': 'id', 'M': 'id', 'N': 'id', 'O': 'id', 'P': 'id', 'Q': 'id', 'R': 'id', 'S': 'id', 'T': 'id',
            'U': 'id', 'V': 'id', 'X': 'id', 'Y': 'id', 'Z': 'id', '_': 'id'
        }
        return switcher.get(analysis, 'ERRO')

    def mudandoOEstadoConformeLeitura(self, caracterLido, estadoAnterior):
        self.estadosExistentes = {'s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13',
                                  's14', 's15', 's16', 's17'}
        if self.realizacaoDeClassificacao(caracterLido) == 'id':
            if estadoAnterior == 's5':
                return 's5'
            elif estadoAnterior == 's3':
                return 's3'
            else:
                return 's2'
        elif self.realizacaoDeClassificacao(caracterLido) == 'num':
            if estadoAnterior == 's5':
                return 's5'
            elif estadoAnterior == 's3':
                return 's3'
            else:
                return 's1'
        elif self.realizacaoDeClassificacao(caracterLido) == 'Comment':
            if estadoAnterior == 's3':
                return 's4'
            else:
                return 's3'
        elif self.realizacaoDeClassificacao(caracterLido) == 'Literal':
            return 's5'
        elif self.realizacaoDeClassificacao(caracterLido) == 'OPR':
            if caracterLido == '<':
                return 's6'
            elif caracterLido == '>':
                return 's7'
            elif caracterLido == '=':
                if estadoAnterior == 's5':
                    return 's5'
                else:
                    return 's8'
        elif self.realizacaoDeClassificacao(caracterLido) == 'OPM':
            if caracterLido == '+':
                return 's10'
            elif caracterLido == '-':
                if estadoAnterior == 's6':
                    return 's9'
                else:
                    return 's10'
            elif caracterLido == '*':
                return 's10'
            elif caracterLido == '/':
                return 's10'
        elif self.realizacaoDeClassificacao(caracterLido) == 'AB_P':
            return 's11'
        elif self.realizacaoDeClassificacao(caracterLido) == 'FC_P':
            return 's12'
        elif self.realizacaoDeClassificacao(caracterLido) == 'PT_V':
            return 's13'
        elif self.realizacaoDeClassificacao(caracterLido) == 'VIR':
            return 's14'
        elif self.realizacaoDeClassificacao(caracterLido) == '':
            if estadoAnterior == 's5':
                return 's5'
            else:
                return 's16'
        else:
            if estadoAnterior == 's5':
                return 's5'
            else:
                return 's17'
