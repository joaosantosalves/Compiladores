from analisadorLexico import *
from analisadorSemantico import *
from acao import action
from goto import *

class analisadorSintatico:
    def __init__(self):
        self.simbolos = self.simbolosDaAnaliseLexica()
        self.analisadorSemantico = analisadorSemantico()

    def simbolosDaAnaliseLexica(self):
        analisador = analisadorLexico()
        analisador.lexico()
        return analisador.simbolosAnalisados

    def sintatico(self):
        token = 0
        fila = [0]
        while True:
            estado = fila[-1]
            resultadoDaAcao = action(estado, self.simbolos[token]["Token"])
            if resultadoDaAcao[0] == "s":
                fila.append(resultadoDaAcao[1])
                self.analisadorSemantico.filaSemantica.append(self.simbolos[token])
                token += 1
            elif resultadoDaAcao[0] == "r":
                indice = resultadoDaAcao[1]
                for i in range(len(producoes[indice][1])):
                    fila.pop()
                estado = fila[-1]
                fila.append(goto(estado, producoes[indice][0]))
                print(producoes[indice][0], "->", *producoes[indice][1])
                self.analisadorSemantico.semantico(indice + 1, self.simbolos)
            elif resultadoDaAcao[0] == "ACC":
                print(producoes[0][0], "->", *producoes[0][1])
                break
            else:
                if resultadoDaAcao[0] == "Erro":
                    self.analisadorSemantico.analisadorDeErro = 1
                    if resultadoDaAcao[1] == 1:
                        if self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        else:
                            self.simbolos.insert(token, {"Classe": "inicio", "Token": "inicio", "Tipo": "", "Linha": 1, "Coluna": 0})
                            print("Erro de sintaxe: Faltou início na linha ", self.simbolos[token]["Linha"])
                    elif resultadoDaAcao[1] == 2:
                        if self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        else:
                            self.simbolos.insert(token, {"Classe": "varinicio", "Token": "varinicio", "Tipo": "", "Linha": self.simbolos[token - 1]["Linha"]+1,
                                                        "Coluna": 0})
                            print("Erro de sintaxe: faltou varinico na linha", self.simbolos[token]["Linha"])
                    elif resultadoDaAcao[1] == 3:
                        if self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        else:
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token - 1]["Linha"],
                                                        "Coluna": self.simbolos[token - 1]["Coluna"]+1})
                            print("Erro de sintaxe: faltou ponto e virgula na linha", self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                    elif resultadoDaAcao[1] == 4:
                        if self.simbolos[token]['Token'] == 'id':
                            self.simbolos.insert(token, {"Classe": "inteiro", "Token": "inteiro", "Tipo": "int", "Linha": self.simbolos[token + 1]["Linha"],
                                                        "Coluna": self.simbolos[token + 1]["Coluna"]-2})
                            print("Erro de sintaxe: faltou inserir o tipo da variavel na linha", self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'escreva':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token]["Linha"] - 1,
                                                         "Coluna": self.simbolos[token]["Coluna"]})

                            self.simbolos.insert(token, {"Classe": "varfim", "Token": "varfim", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro de sintaxe: Faltou inserir o varfim na linha", self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                    elif resultadoDaAcao[1] == 5:
                        if self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        elif self.simbolos[token]['Token'] == 'inteiro':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 3})
                            self.simbolos.insert(token, {"Classe": "A", "Token": "id", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro: faltou inserir a variavel na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'real':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 3})
                            self.simbolos.insert(token, {"Classe": "A", "Token": "id", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro: faltou inserir a variavel na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'literal':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 3})
                            self.simbolos.insert(token, {"Classe": "A", "Token": "id", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro: faltou inserir a variavel na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'varfim':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 3})
                            self.simbolos.insert(token, {"Classe": "A", "Token": "id", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro: faltou inserir a variavel na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])

                        elif self.simbolos[token]['Token'] == 'Literal':
                            self.simbolos.insert(token, {"Classe": "escreva", "Token": "escreva", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] - 2})
                            print("Erro: faltou inserir o escreva na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token-1]['Token'] == 'Literal':
                            self.simbolos.insert(token+1, {"Classe": ";", "Token": "PT_V", "Tipo": "", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] + 1})
                            token -= 1
                            print("Erro: faltou inserir ponto e virgula na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'RCB':
                            self.simbolos.insert(token, {"Classe": "", "Token": "num", "Tipo": "int", "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] + 1})
                            print("Erro: faltou inserir numero na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif (self.simbolos[token-1]['Token'] == 'id' or self.simbolos[token-1]['Token'] == 'num') and self.simbolos[token-2]['Token'] == 'AB_P':
                            self.simbolos.insert(token, {"Classe": "", "Token": "OPR", "Tipo": "", "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token-1]["Coluna"] + 1})
                            print("Erro: faltou inserir o operador lógico na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'AB_P':
                            self.simbolos.insert(token,
                                                 {"Classe": "se", "Token": "se", "Tipo": "",
                                                  "Linha": self.simbolos[token]["Linha"],
                                                  "Coluna": self.simbolos[token]["Coluna"] - 1})
                            print("Erro: faltou inserir se na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token-2]['Token'] == 'id':
                            if self.simbolos[token]['Token'] == '$':
                                self.simbolos.insert(token, {"Classe": "fim", "Token": "fim", "Tipo": "",
                                                                 "Linha": self.simbolos[token]["Linha"],
                                                                 "Coluna": self.simbolos[token]["Coluna"]})
                                print("Erro: faltou inserir o fim na linha",
                                      self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            else:
                                if self.simbolos[token]['Token'] == 'AB_P':
                                    self.simbolos.insert(token,
                                                         {"Classe": "se", "Token": "se", "Tipo": "",
                                                          "Linha": self.simbolos[token]["Linha"],
                                                          "Coluna": self.simbolos[token]["Coluna"] - 1})
                                    print("Erro: faltou inserir se na linha",
                                          self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                                else:
                                    self.simbolos.insert(token-2, {"Classe": "escreva", "Token": "escreva", "Tipo": "", "Linha": self.simbolos[token-2]["Linha"],
                                                                 "Coluna": self.simbolos[token-2]["Coluna"] - 2})
                                    print("Erro: faltou inserir o escreva na linha",
                                          self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                                    token -= 2
                        elif self.simbolos[token-1]['Token'] == 'Literal':
                            self.simbolos.insert(token, {"Classe": ";", "Token": "PT_V", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 1})
                            print("Erro de sintaxe: faltou ponto e virgula na linha", self.simbolos[token]["Linha"],
                                  " e coluna", self.simbolos[token]["Coluna"])
                        elif (self.simbolos[token-1]['Token'] == 'id' or self.simbolos[token-1]['Token'] == 'num') and self.simbolos[token-2]['Token'] == 'OPR':
                            self.simbolos.insert(token, {"Classe": ")", "Token": "FC_P", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 1})
                            print("Erro: faltou inserir o fecha parênteses na linha", self.simbolos[token]["Linha"],
                                  " e coluna", self.simbolos[token]["Coluna"])
                    elif resultadoDaAcao[1] == 6:
                        if self.simbolos[token]['Token'] == 'leia':
                            self.simbolos.insert(token, {"Classe": "", "Token": "Literal", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 2})
                            print("Erro: faltou inserir a descrição do '"'Literal'"' na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'escreva':
                            self.simbolos.insert(token, {"Classe": "", "Token": "Literal", "Tipo": "",
                                                         "Linha": self.simbolos[token]["Linha"],
                                                         "Coluna": self.simbolos[token]["Coluna"] + 2})
                            print("Erro: faltou inserir a variável ou descrição do '"'Literal'"' na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token-1]['Token'] == 'escreva':
                            self.simbolos.insert(token, {"Classe": "", "Token": "Literal", "Tipo": "",
                                                         "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token-1]["Coluna"] + 2})
                            print("Erro: faltou inserir a variável ou descrição do '"'Literal'"' na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                    elif resultadoDaAcao[1] == 7:
                        if self.simbolos[token-1]['Token'] == 'id':
                            if self.simbolos[token]['Token'] == 'FC_P':
                                self.simbolos.insert(token, {"Classe": "", "Token": "OPR", "Tipo": "",
                                                             "Linha": self.simbolos[token]["Linha"],
                                                             "Coluna": self.simbolos[token]["Coluna"] + 1})
                                print("Erro: faltou inserir operador lógico na linha",
                                      self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            else:
                                self.simbolos.insert(token-1, {"Classe": "leia", "Token": "leia", "Tipo": "",
                                                             "Linha": self.simbolos[token - 1]["Linha"],
                                                             "Coluna": self.simbolos[token - 1]["Coluna"] - 2})
                                print("Erro: faltou inserir leia na linha",
                                      self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                                token -= 1
                                fila.pop()
                        elif self.simbolos[token-1]['Token'] == 'OPM':
                            self.simbolos.insert(token, {"Classe": "", "Token": "num", "Tipo": "int",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 1})
                            print("Erro: faltou inserir um numero na linha",
                                  self.simbolos[token - 1]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        elif self.simbolos[token-1]['Token'] == 'AB_P':
                            self.simbolos.insert(token, {"Classe": "", "Token": "id", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 1})
                            print("Erro: faltou inserir um caracter ou numero na linha",
                                  self.simbolos[token-1]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token-1]['Token'] == 'OPR':
                            self.simbolos.insert(token, {"Classe": "", "Token": "id", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 1})
                            print("Erro: faltou inserir um caracter ou numero na linha",
                                  self.simbolos[token-1]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                    elif resultadoDaAcao[1] == 8:
                        if self.simbolos[token-1]['Token'] == 'leia':
                            self.simbolos.insert(token, {"Classe": "", "Token": "id", "Tipo": "",
                                                         "Linha": self.simbolos[token - 1]["Linha"],
                                                         "Coluna": self.simbolos[token - 1]["Coluna"] + 2})
                            print("Erro: faltou inserir o id apos o leia na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])

                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                    elif resultadoDaAcao[1] == 9:
                        if self.simbolos[token-7]['Token'] == 'fimse':
                            self.simbolos.insert(token, {"Classe": "", "Token": "id", "Tipo": "",
                                                         "Linha": self.simbolos[token - 7]["Linha"] + 1,
                                                         "Coluna": self.simbolos[token - 7]["Coluna"] - 2})
                            print("Erro: faltou inserir fimse na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            fila.pop()
                            fila.pop()
                            token -= 7

                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                        else:
                            return print("Erro: faltou inserir fimse na linha {} e coluna {}".format(self.simbolos[len(self.simbolos)-1]['Linha']-1, 1))
                    elif resultadoDaAcao[1] == 10:
                        if self.simbolos[token]['Token'] == 'escreva':
                            self.simbolos.insert(token, {"Classe": "entao", "Token": "entao", "Tipo": "",
                                                         "Linha": self.simbolos[token]["Linha"] - 1,
                                                         "Coluna": self.simbolos[token]["Coluna"] - 4})
                            print("Erro: faltou inserir entao na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'se':
                            self.simbolos.insert(token, {"Classe": "entao", "Token": "entao", "Tipo": "",
                                                         "Linha": self.simbolos[token]["Linha"] - 1,
                                                         "Coluna": self.simbolos[token]["Coluna"] - 4})
                            print("Erro: faltou inserir entao na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)
                    elif resultadoDaAcao[1] == 11:
                        if self.simbolos[token-1]['Token'] == 'se':
                            self.simbolos.insert(token, {"Classe": "(", "Token": "AB_P", "Tipo": "",
                                                         "Linha": self.simbolos[token-1]["Linha"],
                                                         "Coluna": self.simbolos[token-1]["Coluna"]})
                            print("Erro: faltou inserir abre parênteses na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                        elif self.simbolos[token]['Token'] == 'ERRO':
                            print("Erro: caracter invalido na linha",
                                  self.simbolos[token]["Linha"], " e coluna", self.simbolos[token]["Coluna"])
                            self.simbolos.pop(token)


producoes = [
    ["P'", ["P"]],
    ["P", ["inicio", "V", "A"]],
    ["V", ["varinicio", "LV"]],
    ["LV", ["D", "LV"]],
    ["LV", ["varfim", ";"]],
    ["D", ["TIPO", "L", ";"]],
    ["L", ["id", ",", "L"]],
    ["L", ["id"]],
    ["TIPO", ["int"]],
    ["TIPO", ["real"]],
    ["TIPO", ["lit"]],
    ["A", ["ES", "A"]],
    ["ES", ["leia", "id", ";"]],
    ["ES", ["escreva", "ARG", ";"]],
    ["ARG", ["literal"]],
    ["ARG", ["num"]],
    ["ARG", ["id"]],
    ["A", ["CMD", "A"]],
    ["CMD", ["id", "rcb", "LD", ";"]],
    ["LD", ["OPRD", "opm", "OPRD"]],
    ["LD", ["OPRD"]],
    ["OPRD", ["id"]],
    ["OPRD", ["num"]],
    ["A", ["COND", "A"]],
    ["COND", ["CAB", "CP"]],
    ["CAB", ["se", "(", "EXP_R", ")", "então"]],
    ["EXP_R", ["OPRD", "opr", "OPRD"]],
    ["CP", ["ES", "CP"]],
    ["CP", ["CMD", "CP"]],
    ["CP", ["COND", "CP"]],
    ["CP", ["fimse"]],
    ["A", ["R", "A"]],
    ["R", ["facaAte", "(", "EXP_R", ")", "CP_R"]],
    ["CP_R", ["ES", "CP_R"]],
    ["CP_R", ["CMD", "CP_R"]],
    ["CP_R", ["COND", "CP_R"]],
    ["CP_R", ["fimFaca"]],
    ["A", ["fim"]]
]
