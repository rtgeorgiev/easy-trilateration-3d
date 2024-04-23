import matplotlib.pyplot as plt
import matplotlib.cm
from random import randint
import pandas as pd
from easy_trilateration.model import Point, Circle


def static(history, actual=None, ax=None):
    if ax is None:
        ax = plt.axes()

    x_values = []
    y_values = []
    z_values = []

    sniffers = set()
    to_draw = []

    conNumber = []
    radius = []

    for i, tri in enumerate(history):
        for sniffer in tri.sniffers:
            sniffers.add(sniffer.center)
        x_values.append(tri.result.center.x)
        y_values.append(tri.result.center.y)
        z_values.append(tri.result.center.z)

        if i % 10 == 0:
            to_draw.append(create_circle(tri.result))
            conNumber.append(tri.meta)
            radius.append(tri.result.radius)

        if i == 0:
            for sniff in sniffers:
                to_draw.append(create_point(sniff, color="red"))

    if actual:
        actual_x = [p.x for p in actual]
        actual_y = [p.y for p in actual]
        actual_z = [p.z for p in actual]
        ax.plot(actual_x, actual_y, actual_z, color="green", linewidth=3)

    draw(to_draw)

    data = {'Condition': conNumber, 'Radius': radius}
    df = pd.DataFrame(data, columns=['Condition', 'Radius'])
    df.to_csv('export_dataframe.csv', index=False, header=True)


def create_circle(circle: Circle, color=None, target=False):
    if target:
        color = matplotlib.cm.jet(1000)
    elif color is None:
        color = matplotlib.cm.jet(randint(50, 100))
    add_shape(plt.Circle((circle.center.x, circle.center.y, circle.center.z), color=color, fill=False, zorder=1, radius=circle.radius,
                         alpha=0.8))
    plt.scatter(circle.center.x, circle.center.y, circle.center.z, color=color, s=100, zorder=2)



def create_point(point: Point, color=matplotlib.cm.jet(randint(0, 100))):
    plt.scatter(point.x, point.y, point.z, color=color, s=100, zorder=2)



def add_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def draw(draw_list):
    for item in draw_list:
        if isinstance(item, Circle):
            create_circle(item)
        if isinstance(item, Point):
            create_point(item)
    plt.show()
