import os


class analisadorSemantico:
    def __init__(self):
        self.filaSemantica = []
        self.tx = 0
        self.armazenarEscritaDoCodigo = ""
        self.armazenarLoop = ""
        self.analisadorDeErro = 0

    def gerarArquivo(self):
        with open("programa.c", 'a') as arquivo:
            arquivo.write(self.armazenarEscritaDoCodigo)

    def semantico(self, indiceDaProducoes, tabelaDeSimbolos):

        if indiceDaProducoes == 2:
            cabecalho = "#include<stdio.h> \ntypedef char literal[256]; \nvoid main(void) { \n\t/*----Variaveis temporarias----*/\n"
            for x in range(self.tx):
                cabecalho += "{}int T{};\n".format("\t", x)
            cabecalho += "{}/*------------------------------*/\n".format("\t")
            self.armazenarEscritaDoCodigo = cabecalho + self.armazenarEscritaDoCodigo
            self.armazenarEscritaDoCodigo += "}"
            if(self.analisadorDeErro == 0):
                self.gerarArquivo()

        elif indiceDaProducoes == 5:
            print("LV -> varfim ;")
            self.armazenarEscritaDoCodigo += ("\n\n\n")
            varfim = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "LV", 'Token': varfim["Token"], 'Tipo': varfim["Tipo"], 'Linha': varfim["Linha"],'Coluna': varfim["Linha"]})

        elif indiceDaProducoes == 6:
            print("D -> TIPO L;")
            i = 0
            while i < len(tabelaDeSimbolos):
                if tabelaDeSimbolos[i]['Classe'] == self.filaSemantica[-2]['Classe']:
                    tabelaDeSimbolos[i]['Tipo'] = self.filaSemantica[-2]['Tipo']
                i += 1
            self.filaSemantica.pop()

        elif indiceDaProducoes == 7:
            print("id.tipo = TIPO.tipo")
            self.filaSemantica[-3]["Tipo"] = self.filaSemantica[-2]["Tipo"]
            self.armazenarEscritaDoCodigo += ("{}{} {} ;\n".format("\t", self.filaSemantica[-2]["Tipo"], self.filaSemantica[-3]["Classe"]))
            self.filaSemantica.pop(-2)

        elif indiceDaProducoes == 8:
            print("id.tipo = TIPO.tipo")
            self.filaSemantica[-1]["Tipo"] = self.filaSemantica[-2]["Tipo"]
            self.armazenarEscritaDoCodigo += ("{}{} {} ;\n".format("\t", self.filaSemantica[-2]["Tipo"], self.filaSemantica[-1]["Classe"]))
            self.filaSemantica.pop(-2)

        elif indiceDaProducoes == 9:
            print("TIPO -> inteiro")
            TIPO = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': 'TIPO', 'Token': 'TIPO', 'Tipo': TIPO["Tipo"], 'Linha': TIPO["Linha"], 'Coluna': TIPO["Coluna"]})

        elif indiceDaProducoes == 10:
            print("TIPO -> real")
            TIPO = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': 'TIPO', 'Token': 'TIPO', 'Tipo': TIPO["Tipo"], 'Linha': TIPO["Linha"], 'Coluna': TIPO["Coluna"]})

        elif indiceDaProducoes == 11:
            print("TIPO -> literal")
            TIPO = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': 'TIPO', 'Token': 'TIPO', 'Tipo': TIPO["Tipo"], 'Linha': TIPO["Linha"], 'Coluna': TIPO["Coluna"]})

        elif indiceDaProducoes == 13:
            print("ES -> leia id;")
            PT_V = self.filaSemantica.pop()
            id = self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "ES", 'Token': "", 'Tipo': "", 'Linha': id["Linha"], 'Coluna': id["Coluna"]})
            if id["Tipo"] != '':
                if id["Tipo"] == "literal":
                    self.armazenarEscritaDoCodigo += ('{}scanf("%s", {}'.format("\t", id["Classe"]) + ");\n")
                elif id["Tipo"] == "int":
                    self.armazenarEscritaDoCodigo += ('{}scanf("%d", &{}'.format("\t", id["Classe"]) + ");\n")
                elif id["Tipo"] == "real":
                    self.armazenarEscritaDoCodigo += ('{}scanf("%lf", &{}'.format("\t", id["Classe"]) + ");\n")
            else:
                print("Erro: Variável não declarada na linha {} e coluna {}".format(PT_V["Linha"], PT_V["Coluna"]))
                self.analisadorDeErro = 1

        elif indiceDaProducoes == 14:
            print("ES -> escreva ARG;")
            self.filaSemantica.pop()
            ARG = self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "ES", 'Token': "", 'Tipo': "", 'Linha': ARG["Linha"], 'Coluna': ARG['Coluna']})
            if ARG["Tipo"] == 'literal':
                self.armazenarEscritaDoCodigo += ('{}printf("%s", {});\n'.format("\t", ARG["Classe"]))
            elif ARG["Tipo"] == 'int':
                self.armazenarEscritaDoCodigo += ('{}printf("%d", {});\n'.format("\t", ARG["Classe"]))
            elif ARG["Tipo"] == 'double':
                self.armazenarEscritaDoCodigo += ('{}printf("%lf", {});\n'.format("\t", ARG["Classe"]))
            else:
                if self.filaSemantica[-5]['Token'] == 'facaAte':
                    self.armazenarLoop += '{}printf({});\n'.format("\t", ARG["Classe"])
                else:
                    self.armazenarEscritaDoCodigo += ('{}printf({});\n'.format("\t", ARG["Classe"]))

        elif indiceDaProducoes == 15:
            print("ARG.atributos <- literal.atributos ")
            ARG = self.filaSemantica.pop()
            self.filaSemantica.append(ARG)

        elif indiceDaProducoes == 16:
            print("ARG.atributos <- num.atributos")
            ARG = self.filaSemantica.pop()
            self.filaSemantica.append(ARG)

        elif indiceDaProducoes == 17:
            print("ARG.atributos <- id.atributos")
            ARG = self.filaSemantica.pop()
            if ARG["Tipo"] != '':
                self.filaSemantica.append(ARG)
            else:
                print("Erro: Variável não declarada na linha {} e coluna {}".format(ARG['Linha'], ARG['Coluna']))
                self.analisadorDeErro = 1

        elif indiceDaProducoes == 19:
            print("CMD <- id rcb LD;")
            self.filaSemantica.pop()
            LD = self.filaSemantica.pop()
            rcb = self.filaSemantica.pop()
            id = self.filaSemantica.pop()
            if id["Tipo"] != '':
                if id["Tipo"] == LD["Tipo"]:
                    self.armazenarEscritaDoCodigo += ("{}{} {} {};\n".format("\t",id["Classe"], rcb["Tipo"], LD["Classe"]))
                    self.filaSemantica.append({'Classe': "CMD", 'Token': "Num", 'Tipo': id['Tipo'], 'Linha': id['Linha'], 'Coluna': id['Coluna']})
                else:
                    print("Erro: Tipos diferentes para atribuição na linha {}".format(rcb["Linha"]))
                    self.analisadorDeErro = 1
            else:
                print("Erro: Variável não declarada na linha {} e coluna {}".format(id["Linha"], id['Coluna']))
                self.analisadorDeErro = 1

        elif indiceDaProducoes == 20:
            print("LD <- OPRD opm OPRD;")
            OPRD2 = self.filaSemantica.pop()
            opm = self.filaSemantica.pop()
            OPRD1 = self.filaSemantica.pop()
            if OPRD1["Tipo"] != "literal" and OPRD1["Tipo"] == OPRD2["Tipo"]:
                tx = self.tx
                self.armazenarEscritaDoCodigo += ("{}T{} = {} {} {};\n".format("\t",tx, OPRD1["Classe"], opm["Tipo"], OPRD2["Classe"]))
                self.filaSemantica.append({'Classe': "T{}".format(tx), 'Token': "", 'Tipo': OPRD1["Tipo"], 'Linha': OPRD1["Linha"], 'Coluna': OPRD1["Coluna"]})
                self.tx += 1
            else:
                print("Erro: Operandos com tipos incompatíveis na linha {} e coluna {}".format(opm['Linha'], opm['Coluna']))
                self.analisadorDeErro = 1

        elif indiceDaProducoes == 21:
            print("LD.atributos <- OPRD.atributos ")
            LD = self.filaSemantica.pop()
            self.filaSemantica.append(LD)

        elif indiceDaProducoes == 22:
            print("OPRD.atributos <- id.atributos ")
            OPRD = self.filaSemantica.pop()
            if OPRD["Tipo"] != '':
                self.filaSemantica.append(OPRD)
            else:
                print("Erro: Variável não declarada na linha {} e coluna {}".format(OPRD['Linha'], OPRD['Coluna']))
                self.analisadorDeErro = 1

        elif indiceDaProducoes == 23:
            print("OPRD.tipo <- num.tipo")
            OPRD = self.filaSemantica.pop()
            self.filaSemantica.append(OPRD)

        elif indiceDaProducoes == 25:
            print("COND -> CAB CP")
            CAB = self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.armazenarEscritaDoCodigo += ("\t"+"}\n")
            self.filaSemantica.append({'Classe': "COND", 'Token': "", 'Tipo': "", 'Linha': CAB["Linha"], 'Coluna': CAB["Coluna"]})

        elif indiceDaProducoes == 26:
            print("CAB -> se (EXP_R) então")
            self.filaSemantica.pop()
            self.filaSemantica.pop()
            EXP_R = self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.armazenarEscritaDoCodigo += ("{}if ( {} )\n".format("\t",EXP_R["Classe"]) + "\t{\n")
            self.filaSemantica.append({'Classe': "CAB", 'Token': "", 'Tipo': "", 'Linha': EXP_R["Linha"], 'Coluna': EXP_R["Coluna"]})

        elif indiceDaProducoes == 27:
            print("EXP_R -> OPRD opr OPRD")
            OPRD2 = self.filaSemantica.pop()
            opr = self.filaSemantica.pop()
            OPRD1 = self.filaSemantica.pop()

            if OPRD1["Tipo"] != '' and OPRD2["Tipo"] != '':
                if (OPRD1["Tipo"] == "int" or OPRD1["Tipo"] == 'double') and (OPRD2["Tipo"] == "int" or OPRD2["Tipo"] == 'double'):
                    tx = self.tx
                    self.filaSemantica.append({'Classe': "T{}".format(tx), 'Token': "boolean", 'Tipo': "boolean", 'Linha': OPRD1["Linha"], 'Coluna': OPRD1["Coluna"]})
                    self.armazenarEscritaDoCodigo += ("{}T{} = {} {} {};\n".format("\t",tx, OPRD1["Classe"], opr["Tipo"], OPRD2["Classe"]))
                    self.tx += 1
                else:
                    print("Erro: Operandos com tipos incompatíveis na linha {} e coluna {}".format(opr['Linha'], opr['Coluna']))
                    self.analisadorDeErro = 1
            else:
                print("Erro: Variável não declarada na linha {} e coluna {}".format(opr["Linha"], opr["Coluna"]))
                self.analisadorDeErro = 1
        elif indiceDaProducoes == 33:
            print("R -> facaAte (EXP_R) CP_R ")
            self.filaSemantica.pop()
            self.filaSemantica.pop()
            EXP_R = self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.filaSemantica.pop()
            self.armazenarEscritaDoCodigo += ("{}while ( {} )\n ".format("\t", EXP_R["Classe"]) + "\t{\n")
            self.armazenarEscritaDoCodigo += (self.armazenarLoop)
            self.filaSemantica.append({'Classe': "R", 'Token': "", 'Tipo': "", 'Linha': EXP_R["Linha"], 'Coluna': EXP_R["Coluna"]})
        elif indiceDaProducoes == 34:
            print("CP_R -> ES CP_R ")
            self.filaSemantica.pop()
            CP_R = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "CP_R", 'Token': "", 'Tipo': "", 'Linha': CP_R["Linha"], 'Coluna': CP_R["Coluna"]})
        elif indiceDaProducoes == 35:
            print("CP_R -> CMD CP_R ")
            self.filaSemantica.pop()
            CP_R = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "CP_R", 'Token': "", 'Tipo': "", 'Linha': CP_R["Linha"], 'Coluna': CP_R["Coluna"]})
        elif indiceDaProducoes == 36:
            print("CP_R -> COND CP_R ")
            self.filaSemantica.pop()
            CP_R = self.filaSemantica.pop()
            self.filaSemantica.append({'Classe': "CP_R", 'Token': "", 'Tipo': "", 'Linha': CP_R["Linha"], 'Coluna': CP_R["Coluna"]})
        elif indiceDaProducoes == 37:
            print("CP_R -> fimFaca ")
            CP_R = self.filaSemantica.pop()
            self.filaSemantica.append(CP_R)
            self.armazenarLoop += "\t}\n"
