def Fatorial(fat):

    temp = 0

    if fat > 1:
        temp = fat * Fatorial(fat - 1)
        Fatorial(fat - 1)
        return temp
    else:
        return fat


def Primo(numero):

    for i in range(2, round(numero / 2)):
        if numero % (i) == 0:
            return False
        
    return True
