def pontoDeAcomodacao(array, pv):
    def verificaOvershoot(array1, pv1):
        aux1 = round(pv1 * 0.98, 3)
        aux2 = round(pv1 / 0.98, 3)

        for value in array1:
            if value > aux2 or value < aux1:
                return True
        return False

    aux3 = round(pv * 0.98, 3)
    aux4 = round(pv / 0.98, 3)
    aux = 0
    for i in range(len(array)):
        newArray = array[i:]
        if aux3 <= array[i] <= aux4 and verificaOvershoot(newArray, pv) == False:
            aux = array[i]
            break
    return aux



