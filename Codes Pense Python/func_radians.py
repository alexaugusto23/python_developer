from math import pi, sin


def radians(degrees: float = None, round_num: bool = False, dig_dec: int = 0) -> float:
    """
    Cálcula radianos a patir de de um número de graus, o param round_num arredenda e dig_dec exibe a quantidade de casas decimais.
    :param degrees: float
    :param round_num: bool
    :param dig_dec: int
    :return float
    """
    radians = (degrees / 180.0) * pi
    radians = sin(radians)

    if round_num:
        radians = round(radians, dig_dec)

    return radians

print(radians(45))
print(radians(45,round_num=True))
print(radians(45,round_num=True, dig_dec=2))
print(radians(45,round_num=True, dig_dec=4))