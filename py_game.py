import pygame
from colour import Color


def draw_line(py_game_display_surf_value, x1, y1, x2, y2, color):
    """
    Método responsável por desenhar uma linha reta usando o PyGame de acordo com a posição de dois pontos.
    :param py_game_display_surf_value:
    :param x1: Valor de X no ponto 1.
    :param y1: Valor de Y no ponto 1.
    :param x2: Valor de X no ponto 2.
    :param y2: Valor de Y no ponto 2.
    :param color: Cor que a linha irá ter.
    :return: None
    """
    pygame.draw.line(py_game_display_surf_value, color, (x1, y1), (x2, y2))


def print_py_game(matrix_results, access_points, py_game_display_surf_value):
    """
    Método responsável por desenhar a simulação usando o PyGame.
    :param py_game_display_surf_value:
    :param access_points:
    :param matrix_results: Matrix float contendo os resultados da simulação.
    :return: None.
    """

    matrix_max_value = matrix_results.max()

    # matrix_max_value = -30
    matrix_min_value = -100

    # Lê os valores da matriz que contêm valores calculados e colore
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = get_color_of_interval(matrix_results[x][y], matrix_max_value, matrix_min_value)
            draw_point(py_game_display_surf_value, color, x, y)

    # Printa de vermelho a posição dos Access Points
    for ap in access_points:
        draw_point(py_game_display_surf_value, RED, ap[0], ap[1])

    # draw_floor_plan(floor_plan)

    # Atualiza a janela do PyGame para que exiba a imagem
    pygame.display.update()


def draw_point(py_game_display_surf_value, color, x, y):
    """
    Método responsável por desenhar um ponto usando o PyGame de acordo com a posição (x,y).
    :param py_game_display_surf_value:
    :param color: A cor que irá ser o ponto.
    :param x: Posição do ponto no eixo X.
    :param y: Posição do ponto no eixo Y.
    :return: None.
    """
    pygame.draw.line(py_game_display_surf_value, color, (x, y), (x, y))


def get_color_of_interval(x, max_value=-30, min_value=-100):
    """
    Este método retorna uma cor de acordo com o valor que está entre o intervalo min-max. Em outras palavras,
    este método transforma um número em uma cor dentro de uma faixa informada.
    :param min_value: Valor mínimo do intervalo.
    :param max_value: Valor máximo do intervalo.
    :param x: Valor que está dentro do intervalo e que deseja saber sua cor.
    :return: Retorna uma tupla representando um cor no formato RGB.
    """

    if PAINT_BLACK_BELOW_SENSITIVITY and x < SENSITIVITY:
        return BLACK

    percentage = get_percentage_of_range(min_value, max_value, x)
    color = get_value_in_list(percentage, COLORS)

    return color


def get_value_in_list(percent, list_numbers):
    """
    Método retorna o valor de uma posição de uma lista. A posição é calculada de acordo a porcentagem.
    :param percent: Valor float representando a porcentagem.
    :param list_numbers: Lista com n números.
    :return: Retorna a cor da posição calculada.
    """
    position = (percent / 100) * len(list_numbers)
    if position < 1:
        position = 1
    elif position >= len(list_numbers):
        position = len(list_numbers)
    return hex_to_rgb(list_numbers[int(position - 1)])


def hex_to_rgb(hex_value):
    """
    Método responsável por converter uma cor no formato hexadecial para um RGB.
    :param hex_value: Valor em hexadecimal da cor.
    :return: Tupla representando a cor em formato RGB.
    """
    hex_value = str(hex_value).lstrip('#')
    lv = len(hex_value)
    return tuple(int(hex_value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def get_percentage_of_range(min_value, max_value, x):
    """
    Método responsável por retornar a porcentagem de acordo com um respectivo intervalo.
    :param min_value: Valor mínimo do intervalo.
    :param max_value: Valor máximo do intervalo.
    :param x: Valor que está no intervalo de min-max que deseja saber sua respectiva porcentagem.
    :return: Retorna uma porcentagem que está de acordo com o intervalo min-max.
    """
    return ((x - min_value) / (max_value - min_value)) * 100


def get_color_gradient(steps=250):
    cores = list(Color("red").range_to(Color("green"), steps))
    cores.pop(0)
    cores.pop(len(cores) - 1)
    return cores


if __name__ == '__main__':
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SENSITIVITY = -90

    # Gradiente de cores da visualização gráfica
    COLORS = get_color_gradient(16)  # 64, 32, 24, 16, 8

    PAINT_BLACK_BELOW_SENSITIVITY = True

    WIDTH = 600
    HEIGHT = 223
