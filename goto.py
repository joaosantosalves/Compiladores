def goto(estado, naoTerminal):
    if estado == 0:
        if naoTerminal == "P":
            return 1
    elif estado == 2:
        if naoTerminal == "V":
            return 3
    elif estado == 3:
        if naoTerminal == "A":
            return 4
        elif naoTerminal == "ES":
            return 10
        elif naoTerminal == "CMD":
            return 13
        elif naoTerminal == "COND":
            return 15
        elif naoTerminal == "R":
            return 17
        elif naoTerminal == "CAB":
            return 38
    elif estado == 5:
        if naoTerminal == "LV":
            return 6
        elif naoTerminal == "D":
            return 7
        elif naoTerminal == "TIPO":
            return 12
    elif estado == 7:
        if naoTerminal == "LV":
            return 32
        elif naoTerminal == "D":
            return 7
        elif naoTerminal == "TIPO":
            return 12
    elif estado == 10:
        if naoTerminal == "A":
            return 11
        elif naoTerminal == "ES":
            return 10
        elif naoTerminal == "CMD":
            return 13
        elif naoTerminal == "COND":
            return 15
        elif naoTerminal == "R":
            return 18
        elif naoTerminal == "CAB":
            return 38
    elif estado == 12:
        if naoTerminal == "L":
            return 71
    elif estado == 13:
        if naoTerminal == "A":
            return 14
        elif naoTerminal == "ES":
            return 10
        elif naoTerminal == "CMD":
            return 13
        elif naoTerminal == "COND":
            return 15
        elif naoTerminal == "CAB":
            return 38
    elif estado == 15:
        if naoTerminal == "A":
            return 16
        elif naoTerminal == "COND":
            return 15
        elif naoTerminal == "ES":
            return 10
        elif naoTerminal == "CMD":
            return 13
        elif naoTerminal == "R":
            return 17
        elif naoTerminal == "CAB":
            return 38
    elif estado == 17:
        if naoTerminal == "A":
            return 18
        elif naoTerminal == "COND":
            return 15
        elif naoTerminal == "ES":
            return 10
        elif naoTerminal == "CMD":
            return 13
        elif naoTerminal == "R":
            return 17
        elif naoTerminal == "CAB":
            return 38
    elif estado == 23:
        if naoTerminal == "ARG":
            return 24
    elif estado == 29:
        if naoTerminal == "LD":
            return 30
        elif naoTerminal == "OPRD":
            return 33
    elif estado == 34:
        if naoTerminal == "OPRD":
            return 35
    elif estado == 38:
        if naoTerminal == "CP":
            return 39
        elif naoTerminal == "ES":
            return 40
        elif naoTerminal == "CMD":
            return 74
        elif naoTerminal == "COND":
            return 75
        elif naoTerminal == "CAB":
            return 38
    elif estado == 40:
        if naoTerminal == "ES":
            return 40
        elif naoTerminal == "CMD":
            return 74
        elif naoTerminal == "COND":
            return 75
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP":
            return 61
    elif estado == 42:
        if naoTerminal == "OPRD":
            return 55
        elif naoTerminal == "EXP_R":
            return 43
    elif estado == 44:
        if naoTerminal == "ES":
            return 46
        elif naoTerminal == "CMD":
            return 48
        elif naoTerminal == "COND":
            return 50
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP_R":
            return 45
    elif estado == 46:
        if naoTerminal == "ES":
            return 46
        elif naoTerminal == "CMD":
            return 48
        elif naoTerminal == "COND":
            return 50
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP_R":
            return 47
    elif estado == 48:
        if naoTerminal == "ES":
            return 46
        elif naoTerminal == "CMD":
            return 48
        elif naoTerminal == "COND":
            return 50
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP_R":
            return 49
    elif estado == 50:
        if naoTerminal == "ES":
            return 46
        elif naoTerminal == "CMD":
            return 48
        elif naoTerminal == "COND":
            return 50
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP_R":
            return 51
    elif estado == 54:
        if naoTerminal == "EXP_R":
            return 58
        elif naoTerminal == "OPRD":
            return 55
    elif estado == 56:
        if naoTerminal == "OPRD":
            return 57
    elif estado == 64:
        if naoTerminal == "L":
            return 65
    elif estado == 74:
        if naoTerminal == "ES":
            return 40
        elif naoTerminal == "COND":
            return 75
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP":
            return 76
    elif estado == 75:
        if naoTerminal == "ES":
            return 40
        elif naoTerminal == "CMD":
            return 74
        elif naoTerminal == "CAB":
            return 38
        elif naoTerminal == "CP":
            return 67
