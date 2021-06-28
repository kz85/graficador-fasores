from math import cos, sin, pi


def polar_to_rectangular(modulo, angulo):
    """
    devuelve las coordenadas x y para un fasor dado su modulo y angulo

    angluo debe estar dado en grados
    """
    argumento = angulo * pi / 180

    x = modulo * cos(argumento)
    y = modulo * sin(argumento)

    return x, y
