dia1, hora1 = map(str, input().split(" "))

hora1 = hora1.split(":")

dia1 = int(dia1)
horas1 = int(hora1[0])
minutos1 = int(hora1[1])
segundos1 = int(hora1[2])

dia2, hora2 = map(str, input().split(" "))

hora2 = hora2.split(":")

dia2 = int(dia2)
horas2 = int(hora2[0])
minutos2 = int(hora2[1])
segundos2 = int(hora2[2])

tempo1 = (segundos1) + (60 * minutos1) + (60 * 60 * horas1) + (60 * 60* 24 * dia1)
tempo2 = (segundos2) + (60 * minutos2) + (60 * 60 * horas2) + (60 * 60* 24 * dia2)

if tempo1 >= tempo2:
    print("Data inválida!")
elif dia1 > 31 or dia2 > 31 or dia1 < 1  or dia2 < 1:
    print("Data inválida!")
elif horas1 > 23 or horas2 > 23 or horas1 < 0 or horas2 < 0:
    print("Data inválida!")
elif minutos1 > 60 or minutos2 > 60 or minutos1 < 0 or minutos2 < 0:
    print("Data inválida!")
elif segundos1 > 60 or segundos2 > 60 or segundos1 < 0 or segundos2 < 0:
    print("Data inválida!")
else:
    tempoFinal = tempo2 - tempo1
    diaFinal = 0
    horaFinal = 0
    minFinal = 0
    segFinal = 0

    while tempoFinal // 86400 != 0:
        diaFinal += 1
        tempoFinal -= 86400
    while tempoFinal // 3600 != 0:
        horaFinal += 1
        tempoFinal -= 3600
    while tempoFinal // 60 != 0:
        minFinal += 1
        tempoFinal -= 60

    segFinal = tempoFinal

    print(diaFinal, "dia(s)")
    print(horaFinal, "hora(s)")
    print(minFinal, "minuto(s)")
    print(segFinal, "segundo(s)")