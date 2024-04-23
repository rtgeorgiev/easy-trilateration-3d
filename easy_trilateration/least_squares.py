import numpy as np
import pandas as pd
from scipy.optimize import least_squares, OptimizeResult
from easy_trilateration.model import Circle, Trilateration 


def solve_history_linear(history: [Trilateration]):
    for item in history:
        solve_linear(item)


def solve_history(history: [Trilateration]):
    guess = Circle(0, 0, 0, 0)  # Initialize guess with 3D coordinates
    cond = []
    for item in history:
        guess = solve(item, guess)
        cond.append(item.meta)
    print("Max:" + str(max(cond)))
    print("Min:" + str(min(cond)))


def solve_linear(trilateration: Trilateration) -> Circle:
    result = linear_least_squares(trilateration.sniffers)
    trilateration.result = result
    trilateration.meta = 1
    return result


def solve(trilateration: Trilateration, guess: Circle = Circle(0, 0, 0, 0)) -> Circle:
    result, meta = easy_least_squares(trilateration.sniffers, guess)
    cov_matrix = pd.DataFrame((meta.jac.transpose().dot(meta.jac)) ** -1)
    trilateration.result = result
    eig = np.linalg.eig(cov_matrix)[0]
    meta = abs(max(eig) / min(eig))
    trilateration.meta = meta
    return result


def rssi_to_distance(rssi, C=35.5510920, N=29.0735592, B=11.8099735):
    return B ** (-1 * (rssi + C) / N)


def linear_least_squares(crls: [Circle]) -> Circle:
    x, y, z = 0, 0, 0
    a = []
    b = []
    for circle in crls:
        a.append([1, -2 * circle.center.x, -2 * circle.center.y, -2 * circle.center.z])
        b.append([circle.radius ** 2 - circle.center.x ** 2 - circle.center.y ** 2 - circle.center.z ** 2])

    A = np.array(a)

    x = np.array([x ** 2 + y ** 2 + z ** 2, x, y, z])

    np.dot(A, x)

    B = np.array(b)

    x, residuals, rank, s = np.linalg.lstsq(A, B)

    return Circle(x[1], x[2], x[3], 0)


def easy_least_squares(trilateration: Trilateration, guess=Circle(0, 0, 0, 0)) -> tuple[Circle, OptimizeResult]:
    crls = trilateration.sniffers  # Extract circles from Trilateration object
    g = (guess.center.x, guess.center.y, guess.center.z, guess.radius)
    result = least_squares(equations, g, args=[crls])

    xf, yf, zf, rf = result.x

    return Circle(xf, yf, zf, rf), result



def equations(guess, crls: [Circle]):
    eqs = []
    x, y, z, r = guess
    for circle in crls:
        eqs.append(((x - circle.center.x) ** 2 + (y - circle.center.y) ** 2 + (z - circle.center.z) ** 2 - (circle.radius - r) ** 2))
    return eqs
