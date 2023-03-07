def avaliacao(notaExercicios, notaTrabalhos):
    notaFinal = (0.4 * notaExercicios) + (0.6 * notaTrabalhos)
    if notaFinal == 0:
        return (notaFinal, 'SR')

    elif notaFinal <= 2.9:
        return (notaFinal, 'II')

    elif notaFinal <= 4.9:
        return (notaFinal, 'MI')

    elif notaFinal <= 6.9:
        return (notaFinal, 'MM')

    elif notaFinal <= 8.9:
        return (notaFinal, 'MS')

    else:
        return (notaFinal, 'SS')
