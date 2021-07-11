import matplotlib.pyplot as plt

from easy_trilateration.model import *
from easy_trilateration.least_squares import *
from easy_trilateration.graph import *


def trilateration_example():
    arr = [Circle(100, 100, 50),
           Circle(100, 50, 50),
           Circle(50, 50, 50),
           Circle(50, 100, 50)]
    result, meta = easy_least_squares(arr)
    create_circle(result, target=True)
    draw(arr)


def history_example() -> [Trilateration]:
    arr = Trilateration([Circle(100, 100, 70.5),
                         Circle(100, 50, 50),
                         Circle(50, 50, 0),
                         Circle(50, 100, 50)])

    arr2 = Trilateration([Circle(100, 100, 50),
                          Circle(100, 50, 70.5),
                          Circle(50, 50, 50),
                          Circle(50, 100, 0)])

    arr3 = Trilateration([Circle(100, 100, 0),
                          Circle(100, 50, 50),
                          Circle(50, 50, 70.5),
                          Circle(50, 100, 50)])

    arr4 = Trilateration([Circle(100, 100, 50),
                          Circle(100, 50, 0),
                          Circle(50, 50, 50),
                          Circle(50, 100, 70.5)])

    hist: [Trilateration] = [arr, arr2, arr3, arr4, arr]

    solve_history(hist)

    _a = animate(hist)
    return _a


if __name__ == '__main__':
    #  trilateration_example()
    a = history_example()
