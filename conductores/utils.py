from math import sqrt


def distancia_entre_dos_puntos(punto_1,punto_2):
    x1 = punto_1[0]
    y1 = punto_1[1]

    x2 = punto_2[0]
    y2 = punto_2[1]

    distancia = sqrt( (x1-x2)**2 + (y1-y2)**2 )

    return distancia