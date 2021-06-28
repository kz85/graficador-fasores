from math import cos, sin, pi, sqrt, atan2


def polar_to_rectangular(modulo, angulo):
    """
    devuelve las coordenadas x y para un fasor dado su modulo y angulo

    angluo debe estar dado en grados
    """
    argumento = angulo * pi / 180

    x = modulo * cos(argumento)
    y = modulo * sin(argumento)

    return x, y


def rectangular_to_polar(x, y):
    """
    devuelve las componentes modulo y angulo para un fasor dadas sus coordenadas x y
    """
    modulo = sqrt(x**2 + y**2)

    angulo = atan2(x / y)  # Angulo está en radianes

    return modulo, angulo
