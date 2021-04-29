def accommodationPoint(array, pv):
    def temOvershoot(array1, pv1):
        aux1 = round(pv1 * 0.98, 3)
        aux2 = round(pv1 / 0.98, 3)

        for value in array1:
            if value > aux2 or value < aux1:
                return True
        return False

    valorPossivel1 = round(pv * 0.98, 3)
    valorPossivel2 = round(pv / 0.98, 3)
    aux = 0
    for i in range(len(array)):
        newArray = array[i:]
        if valorPossivel1 <= array[i] <= valorPossivel2 and temOvershoot(newArray, pv) == False:
            aux = array[i]
            break
    return aux



