def action(estado, token):
    if estado == 0:
        if token == "inicio":
            return ["s", 2]
        else:
            return ["Erro", 1]
    if estado == 1:
        if token == "$":
            return ["ACC", 0]
        else:
            return ["Erroo", 0]
    if estado == 2:
        if token == "varinicio":
            return ["s", 5]
        else:
            return ["Erro", 2]
    if estado == 3:
        if token == "id":
            return ["s", 28]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        elif token == "fim":
            return ["s", 19]
        elif token == "facaAte":
            return ["s", 41]
        else:
            return ["Erro", 0]
    if estado == 4:
        if token == "id":
            return ["r", 1]
        elif token == "leia":
            return ["r", 1]
        elif token == "escreva":
            return ["r", 1]
        elif token == "se":
            return ["r", 1]
        elif token == "fimse":
            return ["r", 1]
        elif token == "$":
            return ["r", 1]
        else:
            return ["Erro", 0]
    if estado == 5:
        if token == "varfim":
            return ["s", 8]
        elif token == "inteiro":
            return ["s", 68]
        elif token == "real":
            return ["s", 69]
        elif token == "lit":
            return ["s", 70]
        else:
            return ["Erro", 4]
    if estado == 6:
        if token == "id":
            return ["r", 2]
        elif token == "leia":
            return ["r", 2]
        elif token == "escreva":
            return ["r", 2]
        elif token == "se":
            return ["r", 2]
        elif token == "fimse":
            return ["r", 2]
        elif token == "PT_V":
            return ["r", 2]
        else:
            return ["Erro", 0]
    if estado == 7:
        if token == "varfim":
            return ["s", 8]
        elif token == "inteiro":
            return ["s", 68]
        elif token == "real":
            return ["s", 69]
        elif token == "lit":
            return ["s", 70]
        else:
            return ["Erro", 4]
    if estado == 8:
        if token == "PT_V":
            return ["s", 9]
        else:
            return ["Erro", 3]
    if estado == 9:
        if token == "id":
            return ["r", 4]
        elif token == "leia":
            return ["r", 4]
        elif token == "escreva":
            return ["r", 4]
        elif token == "se":
            return ["r", 4]
        elif token == "fimse":
            return ["r", 4]
        elif token == "PT_V":
            return ["r", 4]
        else:
            return ["Erro", 5]
    if estado == 10:
        if token == "id":
            return ["s", 28]
        elif token == "fim":
            return ["s", 19]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        elif token == "facaAte":
            return ["s", 41]
        else:
            return ["Erro", 19]
    if estado == 11:
        if token == "id":
            return ["r", 11]
        elif token == "leia":
            return ["r", 11]
        elif token == "escreva":
            return ["r", 11]
        elif token == "se":
            return ["r", 11]
        elif token == "fimse":
            return ["r", 11]
        elif token == "fim":
            return ["r", 11]
        elif token == "$":
            return ["r", 11]
        else:
            return ["Erro", 21]
    if estado == 12:
        if token == "id":
            return ["s", 63]
        else:
            return ["Erro", 11]
    if estado == 13:
        if token == "id":
            return ["s", 28]
        elif token == "fim":
            return ["s", 19]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        elif token == "facaAte":
            return ["s", 41]
        else:
            return ["Erroo", 0]
    if estado == 14:
        if token == "id":
            return ["r", 17]
        elif token == "leia":
            return ["r", 17]
        elif token == "escreva":
            return ["r", 17]
        elif token == "se":
            return ["r", 17]
        elif token == "fimse":
            return ["r", 17]
        elif token == "fim":
            return ["r", 17]
        elif token == "$":
            return ["r", 17]
        else:
            return ["Erro", 22]
    if estado == 15:
        if token == "id":
            return ["s", 28]
        elif token == "fim":
            return ["s", 19]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        elif token == "facaAte":
            return ["s", 41]
        else:
            return ["Erroo", 0]
    if estado == 16:
        if token == "id":
            return ["r", 23]
        elif token == "leia":
            return ["r", 23]
        elif token == "escreva":
            return ["r", 23]
        elif token == "se":
            return ["r", 23]
        elif token == "fimse":
            return ["r", 23]
        elif token == "fim":
            return ["r", 23]
        elif token == "$":
            return ["r", 23]
        else:
            return ["Erro", 22]
    if estado == 17:
        if token == "id":
            return ["s", 28]
        elif token == "fim":
            return ["s", 19]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        elif token == "faceAte":
            return ["s", 41]
        else:
            return ["Erroo", 0]
    if estado == 18:
        if token == "id":
            return ["r", 31]
        elif token == "leia":
            return ["r", 31]
        elif token == "escreva":
            return ["r", 31]
        elif token == "se":
            return ["r", 31]
        elif token == "fimse":
            return ["r", 31]
        elif token == "fim":
            return ["r", 31]
        elif token == "$":
            return ["r", 31]
        else:
            return ["Erro", 22]
    if estado == 19:
        if token == "id":
            return ["r", 37]
        elif token == "leia":
            return ["r", 37]
        elif token == "escreva":
            return ["r", 37]
        elif token == "se":
            return ["r", 37]
        elif token == "fimse":
            return ["r", 37]
        elif token == "$":
            return ["r", 37]
        else:
            return ["Erro", 5]
    if estado == 20:
        if token == "id":
            return ["s", 21]
        else:
            return ["Erro", 8]
    if estado == 21:
        if token == "PT_V":
            return ["s", 22]
        else:
            return ["Erro", 3]
    if estado == 22:
        if token == "id":
            return ["r", 12]
        elif token == "leia":
            return ["r", 12]
        elif token == "escreva":
            return ["r", 12]
        elif token == "se":
            return ["r", 12]
        elif token == "fimse":
            return ["r", 12]
        else:
            return ["Erro", 5]
    if estado == 23:
        if token == "id":
            return ["s", 27]
        elif token == "num":
            return ["s", 26]
        elif token == "Literal":
            return ["s", 25]
        else:
            return ["Erro", 6]
    if estado == 24:
        if token == "PT_V":
            return ["s", 73]
        else:
            return ["Erro", 3]
    if estado == 25:
        if token == "id":
            return ["r", 14]
        elif token == "leia":
            return ["r", 14]
        elif token == "escreva":
            return ["r", 14]
        elif token == "se":
            return ["r", 14]
        elif token == "fimse":
            return ["r", 14]
        elif token == "PT_V":
            return ["r", 14]
        else:
            return ["Erro", 5]
    if estado == 26:
        if token == "id":
            return ["r", 15]
        elif token == "leia":
            return ["r", 15]
        elif token == "escreva":
            return ["r", 15]
        elif token == "se":
            return ["r", 15]
        elif token == "fimse":
            return ["r", 15]
        elif token == "PT_V":
            return ["r", 14]
        else:
            return ["Erro", 5]
    if estado == 27:
        if token == "id":
            return ["r", 16]
        elif token == "leia":
            return ["r", 16]
        elif token == "escreva":
            return ["r", 16]
        elif token == "se":
            return ["r", 16]
        elif token == "fimse":
            return ["r", 16]
        elif token == "PT_V":
            return ["r", 16]
        else:
            return ["Erro", 5]
    if estado == 28:
        if token == "RCB":
            return ["s", 29]
        else:
            return ["Erro", 7]
    if estado == 29:
        if token == "id":
            return ["s", 36]
        elif token == "num":
            return ["s", 37]
        else:
            return ["Erro", 7]
    if estado == 30:
        if token == "PT_V":
            return ["s", 31]
        else:
            return ["Erro", 3]
    if estado == 31:
        if token == "id":
            return ["r", 18]
        elif token == "leia":
            return ["r", 18]
        elif token == "escreva":
            return ["r", 18]
        elif token == "se":
            return ["r", 18]
        elif token == "fimse":
            return ["r", 18]
        elif token == "fimFaca":
            return ["r", 18]
        else:
            return ["Erro", 5]
    if estado == 32:
        if token == "id":
            return ["r", 3]
        elif token == "leia":
            return ["r", 3]
        elif token == "escreva":
            return ["r", 3]
        elif token == "se":
            return ["r", 3]
        elif token == "fimse":
            return ["r", 3]
        elif token == "fimse":
            return ["r", 3]
        elif token == "PT_V":
            return ["r", 3]
        else:
            return ["Erro", 5]
    if estado == 33:
        if token == "OPM":
            return ["s", 34]
        elif token == "PT_V":
            return ["r", 20]
        else:
            return ["Erro", 7]
    if estado == 34:
        if token == "id":
            return ["s", 36]
        elif token == "num":
            return ["s", 37]
        else:
            return ["Erro", 7]
    if estado == 35:
        if token == "id":
            return ["r", 19]
        elif token == "leia":
            return ["r", 19]
        elif token == "escreva":
            return ["r", 19]
        elif token == "se":
            return ["r", 19]
        elif token == "fimse":
            return ["r", 19]
        elif token == "PT_V":
            return ["r", 19]
        else:
            return ["Erro", 5]
    if estado == 36:
        if token == "id":
            return ["r", 21]
        elif token == "leia":
            return ["r", 21]
        elif token == "escreva":
            return ["r", 21]
        elif token == "se":
            return ["r", 21]
        elif token == "fimse":
            return ["r", 21]
        elif token == "OPR":
            return ["r", 21]
        elif token == "OPM":
            return ["r", 21]
        elif token == "PT_V":
            return ["r", 21]
        elif token == "FC_P":
            return ["r", 21]
        else:
            return ["Erro", 5]
    if estado == 37:
        if token == "id":
            return ["r", 22]
        elif token == "leia":
            return ["r", 22]
        elif token == "escreva":
            return ["r", 22]
        elif token == "se":
            return ["r", 22]
        elif token == "fimse":
            return ["r", 22]
        elif token == "FC_P":
            return ["r", 22]
        elif token == "PT_V":
            return ["r", 22]
        else:
            return ["Erro", 5]
    if estado == 38:
        if token == "id":
            return ["s", 28]
        elif token == "fimse":
            return ["s", 62]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 0]
    if estado == 39:
        if token == "id":
            return ["r", 24]
        elif token == "leia":
            return ["r", 24]
        elif token == "escreva":
            return ["r", 24]
        elif token == "se":
            return ["r", 24]
        elif token == "fimse":
            return ["r", 24]
        elif token == "facaAte":
            return ["r", 24]
        elif token == "fimFaca":
            return ["r", 24]
        else:
            return ["Erro", 5]
    if estado == 40:
        if token == "id":
            return ["s", 28]
        elif token == "fimse":
            return ["s", 62]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 0]
    if estado == 41:
        if token == "AB_P":
            return ["s", 42]
        else:
            return ["Erro", 7]
    if estado == 42:
        if token == "id":
            return ["s", 36]
        elif token == "num":
            return ["s", 37]
        else:
            return ["Erro", 7]
    if estado == 43:
        if token == "FC_P":
            return ["s", 44]
        else:
            return ["Erro", 7]
    if estado == 44:
        if token == "id":
            return ["s", 28]
        elif token == "fimFaca":
            return ["s", 52]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 7]
    if estado == 45:
        if token == "id":
            return ["r", 32]
        elif token == "leia":
            return ["r", 32]
        elif token == "escreva":
            return ["r", 32]
        elif token == "se":
            return ["r", 32]
        elif token == "fimse":
            return ["r", 32]
        else:
            return ["Erro", 5]
    if estado == 46:
        if token == "id":
            return ["s", 28]
        elif token == "fimFaca":
            return ["s", 52]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 7]
    if estado == 47:
        if token == "id":
            return ["r", 33]
        elif token == "leia":
            return ["r", 33]
        elif token == "escreva":
            return ["r", 33]
        elif token == "se":
            return ["r", 33]
        elif token == "fimse":
            return ["r", 33]
        else:
            return ["Erro", 15]
    if estado == 48:
        if token == "id":
            return ["s", 28]
        elif token == "fimFaca":
            return ["s", 52]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 7]
    if estado == 49:
        if token == "id":
            return ["r", 34]
        elif token == "leia":
            return ["r", 34]
        elif token == "escreva":
            return ["r", 34]
        elif token == "se":
            return ["r", 34]
        elif token == "fimse":
            return ["r", 34]
        else:
            return ["Erro", 15]
    if estado == 50:
        if token == "id":
            return ["s", 28]
        elif token == "fimFaca":
            return ["s", 52]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 7]
    if estado == 51:
        if token == "id":
            return ["r", 35]
        elif token == "leia":
            return ["r", 35]
        elif token == "escreva":
            return ["r", 35]
        elif token == "se":
            return ["r", 35]
        elif token == "fimse":
            return ["r", 35]
        else:
            return ["Erro", 5]
    if estado == 52:
        if token == "id":
            return ["r", 36]
        elif token == "leia":
            return ["r", 36]
        elif token == "escreva":
            return ["r", 36]
        elif token == "se":
            return ["r", 36]
        elif token == "fimse":
            return ["r", 36]
        else:
            return ["Erro", 5]
    if estado == 53:
        if token == "AB_P":
            return ["s", 54]
        else:
            return ["Erro", 11]
    if estado == 54:
        if token == "id":
            return ["s", 36]
        elif token == "num":
            return ["s", 37]
        else:
            return ["Erro", 7]
    if estado == 55:
        if token == "OPR":
            return ["s", 56]
        else:
            return ["Erro", 7]
    if estado == 56:
        if token == "id":
            return ["s", 36]
        elif token == "num":
            return ["s", 37]
        else:
            return ["Erro", 7]
    if estado == 57:
        if token == "id":
            return ["r", 26]
        elif token == "leia":
            return ["r", 26]
        elif token == "escreva":
            return ["r", 26]
        elif token == "se":
            return ["r", 26]
        elif token == "fimse":
            return ["r", 26]
        elif token == "FC_P":
            return ["r", 26]
        else:
            return ["Erro", 5]
    if estado == 58:
        if token == "FC_P":
            return ["s", 59]
        else:
            return ["Erro", 7]
    if estado == 59:
        if token == "entao":
            return ["s", 60]
        else:
            return ["Erro", 10]
    if estado == 60:
        if token == "id":
            return ["r", 25]
        elif token == "leia":
            return ["r", 25]
        elif token == "escreva":
            return ["r", 25]
        elif token == "se":
            return ["r", 25]
        elif token == "fimse":
            return ["r", 25]
        else:
            return ["Erro", 5]
    if estado == 61:
        if token == "id":
            return ["r", 27]
        elif token == "leia":
            return ["r", 27]
        elif token == "escreva":
            return ["r", 27]
        elif token == "se":
            return ["r", 27]
        elif token == "fimse":
            return ["r", 27]
        elif token == "fimFaca":
            return ["r", 27]
        else:
            return ["Erro", 5]
    if estado == 62:
        if token == "id":
            return ["r", 30]
        elif token == "leia":
            return ["r", 30]
        elif token == "escreva":
            return ["r", 30]
        elif token == "se":
            return ["r", 30]
        elif token == "fimse":
            return ["r", 30]
        elif token == "facaAte":
            return ["r", 30]
        elif token == "fimFaca":
            return ["r", 30]
        else:
            return ["Erro", 5]
    if estado == 63:
        if token == "VIR":
            return ["s", 64]
        elif token == "id":
            return ["r", 7]
        elif token == "lit":
            return ["r", 7]
        elif token == "real":
            return ["r", 7]
        elif token == "inteiro":
            return ["r", 7]
        elif token == "PT_V":
            return ["r", 7]
        else:
            return ["Erro", 5]
    if estado == 64:
        if token == "id":
            return ["s", 63]
        else:
            return ["Erro", 64]
    if estado == 65:
        if token == "PT_V":
            return ["s", 66]
        else:
            return ["Erro", 3]
    if estado == 66:
        if token == "id":
            return ["r", 6]
        elif token == "leia":
            return ["r", 6]
        elif token == "escreva":
            return ["r", 6]
        elif token == "se":
            return ["r", 6]
        elif token == "fimse":
            return ["r", 6]
        else:
            return ["Erro", 5]
    if estado == 67:
        if token == "id":
            return ["r", 29]
        elif token == "leia":
            return ["r", 29]
        elif token == "escreva":
            return ["r", 29]
        elif token == "se":
            return ["r", 29]
        elif token == "fimse":
            return ["r", 29]
        elif token == "facaAte":
            return ["r", 29]
        else:
            return ["Erro", 5]
    if estado == 68:
        if token == "id":
            return ["r", 8]
        elif token == "leia":
            return ["r", 8]
        elif token == "escreva":
            return ["r", 8]
        elif token == "se":
            return ["r", 8]
        elif token == "fimse":
            return ["r", 8]
        elif token == "PT_V":
            return ["r", 8]
        else:
            return ["Erro", 5]
    if estado == 69:
        if token == "id":
            return ["r", 9]
        elif token == "leia":
            return ["r", 9]
        elif token == "escreva":
            return ["r", 9]
        elif token == "se":
            return ["r", 9]
        elif token == "fimse":
            return ["r", 9]
        elif token == "PT_V":
            return ["r", 9]
        else:
            return ["Erro", 5]
    if estado == 70:
        if token == "id":
            return ["r", 10]
        elif token == "leia":
            return ["r", 10]
        elif token == "escreva":
            return ["r", 10]
        elif token == "se":
            return ["r", 10]
        elif token == "fimse":
            return ["r", 10]
        elif token == "PT_V":
            return ["r", 10]
        else:
            return ["Erro", 5]
    if estado == 71:
        if token == "PT_V":
            return ["s", 72]
        else:
            return ["Erro", 3]
    if estado == 72:
        if token == "id":
            return ["r", 5]
        elif token == "leia":
            return ["r", 5]
        elif token == "escreva":
            return ["r", 5]
        elif token == "se":
            return ["r", 5]
        elif token == "fimse":
            return ["r", 5]
        elif token == "varfim":
            return ["r", 5]
        elif token == "inteiro":
            return ["r", 5]
        elif token == "real":
            return ["r", 5]
        elif token == "lit":
            return ["r", 5]
        elif token == "PT_V":
            return ["r", 5]
        else:
            return ["Erro", 5]
    if estado == 73:
        if token == "id":
            return ["r", 13]
        elif token == "leia":
            return ["r", 13]
        elif token == "escreva":
            return ["r", 13]
        elif token == "se":
            return ["r", 13]
        elif token == "fimse":
            return ["r", 13]
        elif token == "fim":
            return ["r", 13]
        elif token == "fimFaca":
            return ["r", 13]
        else:
            return ["Erro", 5]
    if estado == 74:
        if token == "fimse":
            return ["s", 62]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 9]
    if estado == 75:
        if token == "fimse":
            return ["s", 62]
        elif token == "id":
            return ["s", 28]
        elif token == "leia":
            return ["s", 20]
        elif token == "escreva":
            return ["s", 23]
        elif token == "se":
            return ["s", 53]
        else:
            return ["Erro", 7]
    if estado == 76:
        if token == "id":
            return ["r", 28]
        elif token == "leia":
            return ["r", 28]
        elif token == "escreva":
            return ["r", 28]
        elif token == "se":
            return ["r", 28]
        elif token == "fimse":
            return ["r", 28]
        else:
            return ["Erro", 5]