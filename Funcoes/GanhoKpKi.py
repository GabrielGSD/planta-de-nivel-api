def errorCalculate(sp, finalValue):
    return abs(round(sp - finalValue, 2))


def temOvershoot(array, pv):
    valorPossivel1 = round(pv * 0.98, 3)
    valorPossivel2 = round(pv / 0.98, 3)

    for value in array:
        if value > valorPossivel2 or value < valorPossivel1:
            return True

    return False


def accommodationPoint(array, pv):
    valorPossivel1 = round(pv * 0.98, 3)
    valorPossivel2 = round(pv / 0.98, 3)
    aux = 0
    for i in range(len(array)):
        newArray = array[i:]
        if valorPossivel1 <= array[i] <= valorPossivel2 and temOvershoot(newArray, pv) == False:
            aux = array[i]
            break

    return aux


def KpKi(sys):
    # Valores de Kp e Ki calculados a mão pelo método ->
    kp = 7.30010
    ki = 0.44721

    return kp, ki
