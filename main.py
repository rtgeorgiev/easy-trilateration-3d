import matplotlib.pyplot as plt
import pandas as pd
from easy_trilateration.model import *
import argparse
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
    arr = Trilateration([Circle(100, 100, 70.71),
                         Circle(100, 50, 50),
                         Circle(50, 50, 0),
                         Circle(50, 100, 50)])

    arr2 = Trilateration([Circle(100, 100, 50),
                          Circle(100, 50, 70.71),
                          Circle(50, 50, 50),
                          Circle(50, 100, 0)])

    arr3 = Trilateration([Circle(100, 100, 0),
                          Circle(100, 50, 50),
                          Circle(50, 50, 70.71),
                          Circle(50, 100, 50)])

    arr4 = Trilateration([Circle(100, 100, 50),
                          Circle(100, 50, 0),
                          Circle(50, 50, 50),
                          Circle(50, 100, 70.71)])

    hist: [Trilateration] = [arr, arr2, arr3, arr4, arr]

    solve_history(hist)

    _a = animate(hist)
    return _a


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Trilateration solver and 2D grapher')
    parser.add_argument('--file', nargs='?', help='data filename', default='resources/capture_combined.csv')

    args = parser.parse_args()

    _filename = args.file

    file = pd.read_csv("resources/capture_combined.csv")

    temp_tril = []
    history = []
    millis = file['millis'][0]

    node = dict()

    # draws = []
    #  for value in node.values():
    #      draws.append(create_point(value))
    #  draw(draws)
    actual = []
    for _, row in file.iterrows():
        actual.append(Point(float(row['target_x']), float(row['target_y'])))
        if row['node'] == 2 or row['node'] == 4 or row['node'] == 6 or row['node'] == 8 or True:
            if millis == row['millis']:
                temp_tril.append(Circle(float(row['x']), float(row['y']), rssi_to_distance(row['rssi'])))
            else:
                history.append(Trilateration(temp_tril.copy()))
                temp_tril = []
                millis = row['millis']

    solve_history(history)
    _a = static(history, actual)
