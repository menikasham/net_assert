import math
import pytest


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def solution(a, b, c):
    disc = discriminant(a, b, c)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        return root1, root2
    elif disc == 0:
        root = -b / (2 * a)
        return root
    else:
        return 'There are no roots'



